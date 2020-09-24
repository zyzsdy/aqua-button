<template>
  <div class="btn">
    <div class="bg" ref="btnBg"></div>
    <span :class="{'shake': playing}">{{text}}</span>
  </div>
</template>

<script>
import { inject, ref, watch } from 'vue'

export default {
  props: {
    text: {
      type: String
    },
    name: {
      type: String
    }
  },
  setup(props) {
    const btnBg = ref()
    let timer = null

    const voices = inject('voices')
    const playing = ref(false)

    watch(() => {
      for (const i in voices) {
        for (const j in voices[i].voiceList) {
          if (voices[i].voiceList[j].name === props.name) {
            return voices[i].voiceList[j].progress
          }
        }
      }
    }, (val) => {
      if (val === 0) {
        playing.value = false
        timer = setTimeout(() => {
          btnBg.value.style.transition = 'width 0.2s linear'
          btnBg.value.style.width = '0'
        }, 200)
      } else {
        playing.value = true
        clearTimeout(timer)
        timer = null
        btnBg.value.style.transition = 'width 0.25s linear'
        btnBg.value.style.width = val + 5 + '%'
      }
    })

    return {
      btnBg,
      playing
    }
  }
}
</script>

<style lang="stylus" scoped>
.btn
  display flex
  align-items center
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
    background linear-gradient(to right, $sub-color 98%, transparent 100%)

  span
    position relative
    line-height 20px
    padding 5px 15px
    word-break break-all

  &:before
    content ''
    display block
    position absolute
    width 100%
    height 100%
    top 0
    left 0
    pointer-events none
    background-image radial-gradient(circle, $main-color 99%, transparent 100%)
    background-repeat no-repeat
    background-position 50%
    transform scale(0, 1)
    opacity 0

  &:hover
    background $hover-color
    box-shadow 0px 2px 10px 0px $main-color

    span
      animation shake 3s linear infinite

  &:active
    background $active-color

    &:before
      transform scale(2, 1)
      opacity 1
      transition transform 0.6s, opacity 0.2s
      transition-delay 0.2s

.shake
  animation shake 3s linear infinite

@media only screen and (max-width 600px)
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
