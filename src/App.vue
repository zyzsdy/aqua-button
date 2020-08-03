<template>
  <div id="app">
    <v-header />
    <router-view/>
    <control />
  </div>
</template>

<script>
import VHeader from './views/Header'
import Control from './components/Control'
import { provide, reactive } from 'vue'

export default {
  components: {
    VHeader,
    Control
  },
  setup () {
    // 播放状态
    const setting = reactive({
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
body
  margin 0

::-webkit-scrollbar
  width 7px
  height 7px

::-webkit-scrollbar-track
  box-shadow inset 0 0 6px rgba(0, 0, 0, 0.3)
  -webkit-box-shadow inset 0 0 6px rgba(0, 0, 0, 0.3)
  background-color rgba(255,0,128,.404)

::-webkit-scrollbar-thumb
  box-shadow inset 0 0 6px rgba(0, 0, 0, .1)
  -webkit-box-shadow inset 0 0 6px rgba(0, 0, 0, .1)
  background-color #5bc0de

::-webkit-scrollbar-thumb:active
  background-color rgba(255,0,128,.404)
</style>
