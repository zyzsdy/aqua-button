<template>
  <div class="header">
    <div class="logo">⚓️</div>
    <div class="title">{{ $t('info.title') }}</div>
    <template v-for="(btn, index) in btnList">
      <i-btn :key="index" :url="btn.url" :img="btn.img" />
    </template>
    <div class="btn" :title="$t('lang')" @click="changeLang">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M12.87,15.07L10.33,12.56L10.36,12.53C12.1,10.59 13.34,8.36 14.07,6H17V4H10V2H8V4H1V6H12.17C11.5,7.92 10.44,9.75 9,11.35C8.07,10.32 7.3,9.19 6.69,8H4.69C5.42,9.63 6.42,11.17 7.67,12.56L2.58,17.58L4,19L9,14L12.11,17.11L12.87,15.07M18.5,10H16.5L12,22H14L15.12,19H19.87L21,22H23L18.5,10M15.88,17L17.5,12.67L19.12,17H15.88Z"></path></svg>
    </div>
  </div>
</template>

<script>
import { getCurrentInstance, onMounted } from 'vue'
import IBtn from '../components/common/IconBtn'

export default {
  components: {
    IBtn
  },
  setup () {
    const { ctx } = getCurrentInstance()

    const btnList = [
      {
        url: 'https://www.youtube.com/channel/UC1opHUrw8rvnsadT-iGp7Cg?sub_confirm=1',
        img: require('../assets/image/youtube-fill.png')
      },
      {
        url: 'https://twitter.com/minatoaqua',
        img: require('../assets/image/twitter-fill.png')
      },
      {
        url: 'https://space.bilibili.com/375504219',
        img: require('../assets/image/bilibili-fill.png')
      }
    ]

    const changeLang = () => {
      if (ctx.$i18n.locale === 'ja-JP') {
        ctx.$i18n.locale = 'zh-CN'
        localStorage.setItem('lang', 'zh-CN')
        document.title = ctx.$t('info.title')
      } else {
        ctx.$i18n.locale = 'ja-JP'
        localStorage.setItem('lang', 'ja-JP')
        document.title = ctx.$t('info.title')
      }
    }

    onMounted(() => {
      const lang = localStorage.getItem('lang')
      if (lang) ctx.$i18n.locale = lang
      document.title = ctx.$t('info.title')
    })

    return {
      btnList,
      changeLang
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~@/assets/style/base.styl'

.header
  z-index 1
  display flex
  align-items center
  position sticky
  top 0
  height 48px
  background linear-gradient(to right, $main-color, $sub-color), rgba(255, 255, 255, 0.8)
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
    flex-shrink 0
    color #eee
    font-size 20px
    margin-right 10px
    user-select none
  .btn
    flex-shrink 0
    width 35px
    height 35px
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
</style>
