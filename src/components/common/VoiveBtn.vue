<template>
  <div class="btn" :class="{'playing': playing}">
    <div class="bg" ref="bg" :style="{'width': progress + '%'}"></div>
    <span>{{text}}</span>
  </div>
</template>

<script>
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
  }
}
</script>

<style lang="stylus" scoped>
.btn
  position relative
  overflow hidden
  box-sizing border-box
  height 34px
  border-radius 18px
  margin 5px
  color #fff
  background rgba(255,0,128,0.404)
  box-shadow 0px 1px 5px 0px rgba(255,0,128,0.404)
  user-select none
  cursor pointer
  transition box-shadow 0.25s
  .bg
    position relative
    top 0
    left 0
    width 0
    height 100%
    background #5bc0de
  span
    display block
    position relative
    top -100%
    left 0
    line-height 34px
    padding 0 15px
  &:hover
    background rgba(255,0,128,0.35)
    box-shadow 0px 2px 10px 0px rgba(255,0,128,0.404)
    span
      animation shake 3s linear infinite
  &:active
    background rgba(255,0,128,0.5)

.playing
  background #5bc0de
  span
    animation shake 3s linear infinite
  &:hover
    background #5bc0de

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
