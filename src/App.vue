<template>
  <div id="app">
    <v-header />
    <router-view style="min-height: calc(100vh - 48px - 67px)" />
    <control v-if="showControl" />
    <v-footer />
  </div>
</template>

<script>
import { provide, reactive, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import Setting from '@/../public/setting/setting.json'
import VHeader from '@/views/Header.vue'
import Control from '@/views/Control.vue'
import VFooter from '@/views/Footer.vue'

export default {
  components: {
    VHeader,
    Control,
    VFooter
  },
  setup() {
    const playSetting = reactive({
      loading: true,
      error: false,
      nowPlay: null,
      overlap: false,
      autoRandom: false,
      loop: false
    })
    provide('playSetting', playSetting)

    const searchData = reactive({
      value: '',
      list: [],
      index: 0
    })
    provide('searchData', searchData)

    const isShowSearch = ref(false)
    provide('isShowSearch', isShowSearch)

    // 是否显示控制栏
    const route = useRoute()
    const showControl = ref(false)
    watch(route, () => {
      // 路由改变后重置搜索
      isShowSearch.value = false
      if (!isShowSearch.value) {
        searchData.value = ''
        searchData.list.length = 0
      }

      if (route.path === '/') {
        showControl.value = true
      } else {
        showControl.value = false
      }
    })

    if (Setting.console && (Setting.console.text || Setting.console.img)) {
      const text = Setting.console.text || ''
      const size = Setting.console.size || '16px'
      const color = Setting.console.color || ''

      const width = Setting.console.imgWidth || '100%'
      const height = Setting.console.imgHeight || '100%'
      const img = Setting.console.img ? `padding-right:${width};padding-top:${height};background:url('${location.origin}/setting/${Setting.console.img}') no-repeat;background-size:100% 100%` : ''

      console.log(`%c${text}%c `, `font-size:${size};color:${color}`, img)
    }

    return {
      showControl
    }
  }
}
</script>

<style lang="stylus">
body
  margin 0
  -webkit-tap-highlight-color rgba(0, 0, 0, 0)

a
  margin-left 5px
  color #888
  text-decoration none

::-webkit-scrollbar
  width 7px
  height 7px

::-webkit-scrollbar-track
  box-shadow inset 0 0 6px rgba(0, 0, 0, 0.3)
  -webkit-box-shadow inset 0 0 6px rgba(0, 0, 0, 0.3)
  background-color $main-color

::-webkit-scrollbar-thumb
  box-shadow inset 0 0 6px rgba(0, 0, 0, 0.1)
  -webkit-box-shadow inset 0 0 6px rgba(0, 0, 0, 0.1)
  background-color $sub-color

::-webkit-scrollbar-thumb:active
  background-color $main-color
</style>
