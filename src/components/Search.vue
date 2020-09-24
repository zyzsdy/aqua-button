<template>
  <div class="search">
    <input
      type="text"
      v-model="searchData.value"
      @keyup.enter="btnClick"
      @keydown.esc="clear"
      @input="search"
    />
    <div class="total">
      <transition name="slider-left">
        <p
          v-if="searchData.list.length > 0"
        >{{searchData.index > 0 ? `${searchData.index}/${searchData.list.length}` : `${searchData.list.length}`}}</p>
      </transition>
    </div>
    <div class="clear" :style="{'border-radius': searchData.value ? '' : '0 10px 10px 0'}">
      <svg
        @click="clear"
        style="cursor: pointer"
        t="1599129457149"
        v-if="searchData.value.length > 0"
        class="icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="7557"
        width="15"
        height="30"
      >
        <path
          d="M510.4 67.2c-246.6 0-446.5 199.9-446.5 446.5s199.9 446.5 446.5 446.5 446.5-199.9 446.5-446.5S757 67.2 510.4 67.2z m223.9 670.5c-24.1 24.1-63.5 24.1-87.6 0L510.4 601.4 374 737.7c-24.1 24.1-63.5 24.1-87.6 0-24.1-24.1-24.1-63.5 0-87.6l136.3-136.3-136.3-136.4c-24.1-24.1-24.1-63.5 0-87.6 24.1-24.1 63.5-24.1 87.6 0l136.3 136.3 136.3-136.3c24.1-24.1 63.5-24.1 87.6 0 24.1 24.1 24.1 63.5 0 87.6L598 513.7 734.3 650c24.1 24.1 24.1 63.6 0 87.7z"
          p-id="7558"
          fill="#dddddd"
        />
      </svg>
      <svg
        v-else
        t="1599130871274"
        class="icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="8859"
        width="30"
        height="30"
      >
        <path
          d="M995.209792 859.621209c17.352203 17.350157 28.086685 41.318034 28.086685 67.807339 0 52.928466-42.916439 95.869465-95.869465 95.869465-26.463722 0-50.429553-10.734482-67.781756-28.086685l0 0L578.68426 714.24726c-57.097416 33.703613-123.432217 53.401234-194.509019 53.401234-211.783451 0-383.472741-171.688267-383.472741-383.472741S172.390767 0.703011 384.176264 0.703011s383.472741 171.687244 383.472741 383.471718c0 71.076802-19.696598 137.41058-53.402257 194.483436L995.209792 859.621209 995.209792 859.621209zM384.176264 96.54587c-158.831448 0-287.605324 128.772852-287.605324 287.62886 0 158.832472 128.772852 287.606347 287.605324 287.606347S671.781588 543.007201 671.781588 384.17473C671.779541 225.318722 543.008736 96.54587 384.176264 96.54587z"
          p-id="8860"
          fill="#dddddd"
        />
      </svg>
    </div>
    <div v-if="searchData.value" class="next" @click="btnClick">
      <svg
        t="1599206540691"
        class="icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="2962"
        width="30"
        height="30"
      >
        <path
          d="M268.8 876.8c-32 32-32 86.4 0 121.6 32 32 86.4 32 118.4 0l419.2-425.6c32-32 32-86.4 0-121.6L387.2 25.6c-16-16-38.4-25.6-60.8-25.6S284.8 9.6 265.6 25.6c-32 32-32 86.4 0 121.6l275.2 281.6c22.4 25.6 41.6 51.2 41.6 86.4s-22.4 64-41.6 86.4l-272 275.2z"
          fill="#ddd"
          p-id="2963"
        />
      </svg>
    </div>
  </div>
</template>

<script>
import { inject, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { EVENT } from '@/assets/script/option'
import mitt from '@/assets/script/mitt'
import VoiceList from '@/../public/translate/voices.json'

export default {
  setup(props) {
    const { locale } = useI18n()

    const isShowSearch = inject('isShowSearch')

    const searchData = inject('searchData')
    const voiceList = VoiceList.voices

    const clear = () => {
      if (searchData.value.length < 1) {
        isShowSearch.value = false
      }
      searchData.value = ''
      searchData.list.length = 0
    }

    const search = () => {
      searchData.list.length = 0
      if (searchData.value.length < 1) return
      const reg = new RegExp(searchData.value, 'i')
      for (const i in voiceList) {
        const name = voiceList[i].translate[locale.value]
        if (name && reg.test(name)) {
          searchData.list.push(voiceList[i].name)
        }
      }
    }

    watch(() => {
      return searchData.value
    }, (newVal, oldVal) => {
      if (newVal !== oldVal) {
        searchData.index = 0
      }
    })

    const btnClick = () => {
      mitt.emit(EVENT.autoScroll)
    }

    return {
      searchData,
      clear,
      search,
      btnClick
    }
  }
}
</script>

<style lang="stylus" scoped>
.search
  display flex
  align-items center
  justify-content center
  width 200px
  height 30px
  margin 0 10px
  overflow hidden
  transition all 0.3s
  color #888
  background rgba(0, 0, 0, 0) !important

  input
    flex 1
    width 100%
    height 100%
    box-sizing border-box
    border-radius 10px 0 0 10px
    padding 0 2px 0 10px
    border 1px solid #ddd
    border-right none
    color #888
    opacity 1

    &:focus
      outline none

  .total
    display flex
    align-items center
    justify-content center
    box-sizing border-box
    height 100%
    font-size 12px
    background #fff
    border 1px solid #ddd
    border-left none
    border-right none

    p
      margin auto

  .clear
    overflow hidden
    display flex
    align-items center
    justify-content center
    box-sizing border-box
    width 24px
    height 30px
    background #fff
    border 1px solid #ddd
    border-left none
    border-right none

    svg
      width 15px

  .next
    box-sizing border-box
    width 30px
    height 100%
    border-radius 0 10px 10px 0
    border 1px solid #bbb
    border-left none
    cursor pointer
    background $hover-color

    svg
      width 50%
      height 50%
      padding 25%

    &:active
      background $active-color
</style>
