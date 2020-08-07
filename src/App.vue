<template>
  <div id="app">
    <v-header />
    <router-view/>
    <control />
    <v-footer />
  </div>
</template>

<script>
import VHeader from './views/Header'
import Control from './views/Control'
import VFooter from './views/Footer'
import { provide, reactive } from 'vue'

export default {
  components: {
    VHeader,
    Control,
    VFooter
  },
  setup () {
    // 播放状态
    const setting = reactive({
      loading: true,
      error: false,
      nowPlay: null,
      overlap: false,
      autoRandom: false,
      loop: false
    })

    provide('setting', setting)
  }
}
</script>

<style lang="stylus">
@import '~@/assets/style/base.styl'

body
  margin 0
  -webkit-tap-highlight-color rgba(0, 0, 0, 0)

::-webkit-scrollbar
  width 7px
  height 7px

::-webkit-scrollbar-track
  box-shadow inset 0 0 6px rgba(0, 0, 0, 0.3)
  -webkit-box-shadow inset 0 0 6px rgba(0, 0, 0, 0.3)
  background-color $main-color

::-webkit-scrollbar-thumb
  box-shadow inset 0 0 6px rgba(0, 0, 0, .1)
  -webkit-box-shadow inset 0 0 6px rgba(0, 0, 0, .1)
  background-color $sub-color

::-webkit-scrollbar-thumb:active
  background-color $main-color
</style>
