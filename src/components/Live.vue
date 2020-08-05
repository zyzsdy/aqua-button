<template>
  <div class="live-wrapper">
    <card>
      <template v-slot:header>
        <div class="title">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22C6.47,22 2,17.5 2,12A10,10 0 0,1 12,2M12.5,7V12.25L17,14.92L16.25,16.15L11,13V7H12.5Z"></path></svg>
          <div>{{$t('live.title')}}</div>
        </div>
      </template>
      <div class="content">
        <p v-if="(!live && !upcoming) || (live.length === 0 && upcoming.length === 0)" class="title">{{$t('live.noLive')}}</p>
        <div class="default" v-else>
          <template v-for="item in live">
            <div :key="item.id" class="live">
              <l-icon />
              <a :href="item.channel.yt_channel_id ? 'https://www.youtube.com/channel/' + item.channel.yt_channel_id : 'https://live.bilibili.com/' + item.channel.bb_space_id" class="live-title" target="_blank">
                {{item.title}}
                <img :src="item.channel.yt_channel_id ? require('../assets/image/youtube-fill.svg') : require('../assets/image/bilibili-fill.svg')">
              </a>
            </div>
          </template>
          <div class="line" v-if="live.length > 0 && upcoming.length > 0"></div>
          <div class="upcoming-content" v-if="upcoming.length > 0">
            <div>{{$t('live.upcoming')}}:</div>
            <template v-for="item in upcoming">
              <div :key="item.id" class="upcoming">
                <div>
                  <div class="upcoming-time">{{new Date(item.live_schedule).toLocaleString()}}</div>
                  <a :href="item.channel.yt_channel_id ? 'https://www.youtube.com/channel/' + item.channel.yt_channel_id : 'https://live.bilibili.com/' + item.channel.bb_space_id" class="upcoming-title" target="_blank">
                    {{item.title}}
                    <img :src="item.channel.yt_channel_id ? require('../assets/image/youtube-fill.svg') : require('../assets/image/bilibili-fill.svg')">
                  </a>
                </div>
              </div>
            </template>
          </div>
        </div>
      </div>
    </card>
  </div>
</template>

<script>
import Card from './common/Card'
import LIcon from './common/LiveIcon'
import axios from 'axios'
import { ref, getCurrentInstance, onMounted } from 'vue'

export default {
  components: {
    Card,
    LIcon
  },
  setup () {
    const { ctx } = getCurrentInstance()

    const title = ref(null)
    const live = ref(null)
    const upcoming = ref(null)

    onMounted(() => {
      title.value = ctx.$t('live.title')

      axios.get('https://api.konkon.icu/v1/live?channel_id=30')
        .then(res => {
          if (res.status === 200) {
            live.value = res.data.live
            upcoming.value = res.data.upcoming
          }
        })
        .catch(() => {
          title.value = ctx.$t('live.error')
        })
    })

    return {
      title,
      live,
      upcoming
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~@/assets/style/base.styl'

.live-wrapper
  margin 10px auto
  .title
    display flex
    align-items center
    height 40px
    margin-left 10px
    div
      font-size 20px
      margin-left 10px
    svg
      fill $main-color
  .content
    padding 10px
    .title
      margin 10px
    .default
      padding 10px
    .live
      display flex
      align-items center
      .live-title
        display flex
        align-items center
        color $main-color
        margin 10px
        user-select none
        cursor pointer
        text-decoration none
        img
          width 30px
          height 30px
    .line
      border-top 1px solid #ddd
      margin-top 10px
      padding-top 10px
    .upcoming-content
      font-size 15px
      .upcoming
        display flex
        align-items center
        .upcoming-time
          margin 10px 0 5px 0
          font-size 12px
        .upcoming-title
          display flex
          align-items center
          color $sub-color
          user-select none
          cursor pointer
          text-decoration none
          img
            width 25px
            height 25px
</style>
