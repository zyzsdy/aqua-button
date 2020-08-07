<template>
  <div class="control">
    <div class="playing" ref="titleRef">
      <transition name="fade">
        <loading v-if="setting.nowPlay && setting.loading" class="tip" />
      </transition>
      <transition name="fade-delay">
        <error v-if="setting.nowPlay && setting.error" class="tip" />
      </transition>
      {{title}}
    </div>
    <div class="btn">
      <div class="icon" :title="$t('action.randomplay')" @click="randomPlay">
        <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="M689.066667 170.666667c-40.533333 0-132.266667 19.2-177.066667 119.466666C467.2 189.866667 377.6 170.666667 334.933333 170.666667 211.2 170.666667 128 266.666667 128 373.333333 128 631.466667 512 853.333333 512 853.333333s384-221.866667 384-480c0-106.666667-83.2-202.666667-206.933333-202.666666z"></path></svg>
      </div>
      <div class="icon" :title="$t('action.stopvoice')" @click="stopPlay">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M18,18H6V6H18V18Z"></path></svg>
      </div>
      <div class="icon" :title="$t('action.overlap')" @click="overlapChange" :class="{'icon-active': setting.overlap}">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M19 3V21H15V3H19M14 3V21H10V3H14M9 3V21H5V3H9Z"></path></svg>
      </div>
      <div class="icon" :title="$t('action.autoRandom')" @click="autoRandomChange" :class="{'icon-active': setting.autoRandom}">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M14.83,13.41L13.42,14.82L16.55,17.95L14.5,20H20V14.5L17.96,16.54L14.83,13.41M14.5,4L16.54,6.04L4,18.59L5.41,20L17.96,7.46L20,9.5V4M10.59,9.17L5.41,4L4,5.41L9.17,10.58L10.59,9.17Z"></path></svg>
      </div>
      <div class="icon" :title="$t('action.loop')" @click="loopChange" :class="{'icon-active': setting.loop}">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M17,17H7V14L3,18L7,22V19H19V13H17M7,7H17V10L21,6L17,2V5H5V11H7V7Z"></path></svg>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, inject, getCurrentInstance, computed, watch } from 'vue'
import mitt from '../assets/js/mitt'
import Loading from '../components/common/Loading'
import Error from '../components/common/Error'

export default {
  components: {
    Loading,
    Error
  },
  setup () {
    const { ctx } = getCurrentInstance()

    const setting = inject('setting')

    const title = computed(() => {
      if (setting.overlap) {
        return ctx.$t('action.overlapTip')
      } else if (setting.nowPlay) {
        return ctx.$t('voice.' + setting.nowPlay.name)
      } else if (setting.autoRandom) {
        return ctx.$t('action.autoRandomTip')
      } else if (setting.loop) {
        return ctx.$t('action.loopTip')
      } else {
        return ctx.$t('action.noplay')
      }
    })

    const titleRef = ref(null)

    let timer = null

    watch(() => {
      return setting.error
    }, () => {
      if (setting.error) {
        timer = setTimeout(() => {
          titleRef.value.style.textDecoration = 'line-through'
        }, 500)
      } else {
        clearTimeout(timer)
        timer = null
        titleRef.value.style.textDecoration = 'none'
      }
    })

    const randomPlay = () => {
      mitt.emit('randomPlay')
    }

    const stopPlay = () => {
      mitt.emit('stopPlay')
    }

    const overlapChange = () => {
      setting.autoRandom = false
      setting.loop = false
      setting.overlap = !setting.overlap
    }

    const autoRandomChange = () => {
      setting.overlap = false
      setting.loop = false
      setting.autoRandom = !setting.autoRandom
    }

    const loopChange = () => {
      setting.overlap = false
      setting.autoRandom = false
      setting.loop = !setting.loop
    }

    return {
      titleRef,
      title,
      setting,
      randomPlay,
      stopPlay,
      overlapChange,
      autoRandomChange,
      loopChange
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~@/assets/style/base.styl'

.control
  display flex
  flex-direction column
  align-items center
  justify-content center
  position sticky
  bottom 0
  background rgba(255, 255, 255, 0.7)
  .playing
    position relative
    margin 10px 0
    max-width 80%
    line-height 21px
    text-align center
    color $title-color
    .tip
      position absolute
      left -23px
      top 0
      height 100%
  .btn
    display flex
    align-items center
    justify-content center
    margin-bottom 10px
    .icon
      width 30px
      height 30px
      margin 0 5px
      border-radius 50%
      background $main-color
      cursor pointer
      svg
        height 80%
        width 80%
        padding 10%
        fill #fff
      &:hover
        box-shadow 0px 0px 10px 0px $sub-color
      &:active
        background $title-color
    .icon-active
      background $sub-color

.fade-enter-active, .fade-leave-active
  transition opacity 0.5s
.fade-enter, .fade-leave-to
  opacity 0
.fade-enter-to, .fade-leave
  opacity 1
</style>
