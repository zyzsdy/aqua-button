<template>
  <transition name="slider-down" appear>
    <div class="header">
      <transition name="logo" appear>
        <div class="logo" ref="logo" @click="logoClick">🌶️</div>
      </transition>
      <router-link :to="titlePath">
        <div class="title">{{ headerTitle }}</div>
      </router-link>
      <template v-for="(btn, index) in btnList" :key="index">
        <i-btn v-if="btn.url" :url="btn.url" :img="btn.img" />
      </template>
      <div class="search-btn" @click="showSearch" v-if="showSearchBtn">
        <svg
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
          />
        </svg>
      </div>
      <search class="search" v-if="showSearchBtn" />
      <div class="btn" :title="t(INFO_I18N.lang)" @click="changeLang">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          height="24"
          width="24"
          role="img"
          aria-hidden="true"
        >
          <path
            d="M12.87,15.07L10.33,12.56L10.36,12.53C12.1,10.59 13.34,8.36 14.07,6H17V4H10V2H8V4H1V6H12.17C11.5,7.92 10.44,9.75 9,11.35C8.07,10.32 7.3,9.19 6.69,8H4.69C5.42,9.63 6.42,11.17 7.67,12.56L2.58,17.58L4,19L9,14L12.11,17.11L12.87,15.07M18.5,10H16.5L12,22H14L15.12,19H19.87L21,22H23L18.5,10M15.88,17L17.5,12.67L19.12,17H15.88Z"
          />
        </svg>
      </div>
    </div>
  </transition>
</template>

<script>
import { ref, inject, onMounted, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRoute } from 'vue-router'
import { INFO_I18N } from '@/assets/script/option'
import IBtn from '@/components/common/IconBtn'
import Search from '@/components/Search'
import Setting from '@/../public/setting/setting.json'

export default {
  components: {
    IBtn,
    Search
  },
  setup() {
    const searchData = inject('searchData')

    const btnList = [
      {
        url: Setting.header.youtube || false,
        img: require('../assets/image/youtube-fill.png')
      },
      {
        url: Setting.header.twitter || false,
        img: require('../assets/image/twitter-fill.png')
      },
      {
        url: Setting.header.bilibili || false,
        img: require('../assets/image/bilibili-fill.png')
      }
    ]

    const logo = ref()
    let isRestart = false
    const logoClick = () => {
      if (!logo.value) return
      if (isRestart) {
        logo.value.style.animation = 'logo 1s'
        isRestart = !isRestart
      } else {
        logo.value.style.animation = 'logo-restart 1s'
        isRestart = !isRestart
      }
    }

    const isShowSearch = inject('isShowSearch')

    const route = useRoute()

    const titlePath = computed(() => {
      return route.path === '/' ? '/search' : '/'
    })

    const showSearch = () => {
      isShowSearch.value = !isShowSearch.value
      if (!isShowSearch.value) {
        searchData.value = ''
        searchData.list.length = 0
      }
    }

    const showSearchBtn = computed(() => {
      return route.path === '/' || route.path === '/search'
    })

    const { t, locale } = useI18n()

    const changeLang = () => {
      searchData.value = ''
      searchData.list.length = 0
      if (locale.value === 'ja-JP') {
        locale.value = 'zh-CN'
        localStorage.setItem('lang', 'zh-CN')
        document.title = t(INFO_I18N.title)
      } else {
        locale.value = 'ja-JP'
        localStorage.setItem('lang', 'ja-JP')
        document.title = t(INFO_I18N.title)
      }
    }

    const headerTitle = computed(() => {
      if (route.path === '/search') {
        return '七奈表情'
      } else {
        return t('info.title')
      }
    })

    onMounted(() => {
      const lang = localStorage.getItem('lang')
      if (lang) locale.value = lang
      document.title = t(INFO_I18N.title)
    })

    return {
      btnList,
      logo,
      logoClick,
      titlePath,
      showSearchBtn,
      t,
      changeLang,
      showSearch,
      headerTitle,
      INFO_I18N
    }
  }
}
</script>

<style lang="stylus" scoped>
.header
  z-index 2
  display flex
  align-items center
  position sticky
  top 0
  height 48px
  background linear-gradient(to right, $main-color, $sub-color), rgba(255, 255, 255, 0.8)

  *
    flex-shrink 0

  .logo
    display block
    width 35px
    height 35px
    font-size 25px
    line-height 35px
    margin 0 10px
    text-align center
    user-select none

  .title
    color #eee
    font-size 20px
    margin-right 10px
    user-select none

  .search-btn
    width 30px
    height 30px
    margin 0 5px
    border-radius 50%
    background rgba(255, 255, 255, 0.5)

    svg
      width 60%
      height 60%
      padding 20%
      fill #666

    &:active
      background rgba(255, 255, 255, 0.6)
      box-shadow 0px 0px 10px 0px $sub-color

  .btn
    flex-shrink 0
    width 30px
    height 30px
    margin 0 10px 0 auto
    border-radius 50%
    background rgba(255, 255, 255, 0.5)
    cursor pointer

    svg
      height 70%
      width 70%
      padding 15%
      fill #fff

    &:hover
      box-shadow 0px 0px 5px 0px #fff

    &:active
      background rgba(255, 255, 255, 0.6)

@media only screen and (min-width 550px)
  .search-btn
    display none

@media only screen and (max-width 550px)
  .search-btn
    display block

  .search
    width 0px
    margin 0
    opacity 0
</style>
