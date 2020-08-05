<template>
  <div class="icon">
    <div class="one"></div>
    <div class="two"></div>
    <div  class="three"></div>
  </div>
</template>

<style lang="stylus" scoped>
@import '~@/assets/style/base.styl'

anim()
  width 20%
  height 100%
  margin auto
  background $main-color
  animation live 2s linear infinite
  animation-direction alternate

.icon
  display flex
  width 24px
  height 24px
  .one
    anim()
  .two
    anim()
    animation-delay 250ms
  .three
    anim()
    animation-delay 500ms

@keyframes live
  0%
    height 0
  100%
    height 100%
</style>
