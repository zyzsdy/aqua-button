<template>
  <div class="btn" :class="{'playing': playing}">
    <div class="bg" ref="btnBg"></div>
    <span :class="{'shake': duration !== 0}">{{text}}</span>
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
    duration: {
      type: Number,
      default: 0
    }
  },
  setup (props) {
    const btnBg = ref(null)

    watch(() => {
      return props.duration
    }, () => {
      playAnimation()
    })

    let timer = null

    const reset = () => {
      btnBg.value.style.transition = 'width 0.3s linear'
      btnBg.value.style.width = '0'
    }

    const playAnimation = () => {
      if (props.duration !== 0) {
        btnBg.value.style.transition = `width ${props.duration}s linear`
        btnBg.value.style.width = '100%'
        timer = setTimeout(() => {
          reset()
        }, props.duration * 1000)
      } else {
        if (timer) {
          clearTimeout(timer)
          timer = null
          reset()
        }
      }
    }

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
  box-sizing border-box
  height 34px
  border-radius 18px
  margin 5px
  color $btn-text-color
  background $main-color
  box-shadow 0px 1px 5px 0px $main-color
  user-select none
  cursor pointer
  transition box-shadow 0.25s
  .bg
    position relative
    top 0
    left 0
    width 0
    height 100%
    background $sub-color
  span
    display block
    position relative
    top -100%
    left 0
    line-height 34px
    padding 0 15px
  &:hover
    background $hover-color
    box-shadow 0px 2px 10px 0px $main-color
    span
      animation shake 3s linear infinite
  &:active
    background $active-color

.playing
  background $sub-color
  span
    animation shake 3s linear infinite
  &:hover
    background $sub-color

.shake
  animation shake 3s linear infinite

@keyframes playing
  0%
    width 0
  100%
    width 100%

@keyframes shake
  0%
    line-height 34px
  20%
    line-height 34px
  25%
    line-height 30px
  30%
    line-height 34px
  35%
    line-height 30px
  40%
    line-height 34px
  100%
    line-height 34px
</style>
