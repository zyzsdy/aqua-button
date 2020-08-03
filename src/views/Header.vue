<template>
  <div class="header">
    <div class="logo">⚓️</div>
    <div class="title">{{ $t('info.title') }}</div>
    <a href="https://www.youtube.com/channel/UC1opHUrw8rvnsadT-iGp7Cg?sub_confirm=1" class="icon" target="_blank">
      <img src="../assets/image/youtube-fill.svg">
    </a>
    <a href="https://twitter.com/minatoaqua" class="icon" target="_blank">
      <img src="../assets/image/twitter-fill.svg">
    </a>
    <a href="https://space.bilibili.com/375504219" class="icon" target="_blank">
      <img src="../assets/image/bilibili-fill.svg">
    </a>
    <div class="btn" :title="$t('lang')" @click="changeLang">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M12.87,15.07L10.33,12.56L10.36,12.53C12.1,10.59 13.34,8.36 14.07,6H17V4H10V2H8V4H1V6H12.17C11.5,7.92 10.44,9.75 9,11.35C8.07,10.32 7.3,9.19 6.69,8H4.69C5.42,9.63 6.42,11.17 7.67,12.56L2.58,17.58L4,19L9,14L12.11,17.11L12.87,15.07M18.5,10H16.5L12,22H14L15.12,19H19.87L21,22H23L18.5,10M15.88,17L17.5,12.67L19.12,17H15.88Z"></path></svg>
    </div>
  </div>
</template>

<script>
import { getCurrentInstance, onMounted } from 'vue'

export default {
  setup () {
    const { ctx } = getCurrentInstance()

    const changeLang = () => {
      if (ctx.$i18n.locale === 'ja-JP') {
        ctx.$i18n.locale = 'zh-CN'
        localStorage.setItem('lang', 'zh-CN')
      } else {
        ctx.$i18n.locale = 'ja-JP'
        localStorage.setItem('lang', 'ja-JP')
      }
    }

    onMounted(() => {
      const lang = localStorage.getItem('lang')
      if (lang) ctx.$i18n.locale = lang
    })

    return {
      changeLang
    }
  }
}
</script>

<style lang="stylus" scoped>
.header
  z-index 1
  display flex
  align-items center
  position sticky
  top 0
  height 48px
  background linear-gradient(to right, rgba(255,0,128,.404), #5bc0de), rgba(255, 255, 255, 0.8)
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
    margin-right 20px
    user-select none
  .icon
    width 30px
    height 30px
    margin 0 5px
    border-radius 50%
    background rgba(255, 255, 255, 0.5)
    img
      height 80%
      padding 10%
    &:hover
      box-shadow 0px 0px 10px 0px #5bc0de
      img
        height 90%
        padding 5%
    &:active
      background rgba(255, 255, 255, 0.6)
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
