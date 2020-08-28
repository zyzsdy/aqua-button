<template>
  <div class="btn" :class="{'playing': playing}">
    <div class="bg" ref="btnBg"></div>
    <span :class="{'shake': progress && progress !== 0}">{{text}}</span>
  </div>
</template>

<script>
import { ref, watch } from 'vue'

export default {
  props: {
    text: {
      type: String,
      default: ''
    },
    playing: {
      type: Boolean,
      default: false
    },
    progress: {
      type: Number,
      default: 0
    }
  },
  setup (props) {
    const btnBg = ref(null)
    let timer = null

    watch(() => {
      return props.progress
    }, () => {
      if (props.progress === 0) {
        timer = setTimeout(() => {
          btnBg.value.style.transition = 'width 0.2s linear'
          btnBg.value.style.width = '0'
        }, 100)
      } else {
        clearTimeout(timer)
        timer = null
        btnBg.value.style.transition = 'width 0.25s linear'
        btnBg.value.style.width = props.progress + 5 + '%'
      }
    })

    return {
      btnBg
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~@/assets/style/base.styl'

.btn
  position relative
  overflow hidden
  min-height 34px
  box-sizing border-box
  border-radius 18px
  color $btn-text-color
  background $main-color
  box-shadow 0px 1px 5px 0px $main-color
  user-select none
  cursor pointer
  transition box-shadow 0.25s
  .bg
    position absolute
    top 0
    left 0
    width 0
    min-height 34px
    height 100%
    background $sub-color
  span
    display block
    position relative
    top -100%
    left 0
    line-height 34px
    padding 0 15px
    word-break break-all
  &:hover
    background $hover-color
    box-shadow 0px 2px 10px 0px $main-color
    span
      animation shake 3s linear infinite
  &:active
    background $active-color

.playing
  background $sub-color !important
  span
    animation shake 3s linear infinite !important

.shake
  animation shake 3s linear infinite

@media only screen and (max-width: 600px)
  .btn:hover
    background $main-color
    box-shadow none
    span
      animation none
  .btn:active
    background $active-color

@keyframes playing
  0%
    width 0
  100%
    width 100%

@keyframes shake
  0%
    transform translateY(0px)
  20%
    transform translateY(0px)
  25%
    transform translateY(-4px)
  30%
    transform translateY(0px)
  35%
    transform translateY(-4px)
  40%
    transform translateY(0px)
  100%
    transform translateY(0px)
</style>
