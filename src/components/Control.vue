<template>
  <div class="control">
    <div class="playing">当前没有播放哦~</div>
    <div class="btn">
      <div class="icon">
        <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" width="24" height="24"><path d="M689.066667 170.666667c-40.533333 0-132.266667 19.2-177.066667 119.466666C467.2 189.866667 377.6 170.666667 334.933333 170.666667 211.2 170.666667 128 266.666667 128 373.333333 128 631.466667 512 853.333333 512 853.333333s384-221.866667 384-480c0-106.666667-83.2-202.666667-206.933333-202.666666z"></path></svg>
      </div>
      <div class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M18,18H6V6H18V18Z"></path></svg>
      </div>
      <div class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M14.83,13.41L13.42,14.82L16.55,17.95L14.5,20H20V14.5L17.96,16.54L14.83,13.41M14.5,4L16.54,6.04L4,18.59L5.41,20L17.96,7.46L20,9.5V4M10.59,9.17L5.41,4L4,5.41L9.17,10.58L10.59,9.17Z"></path></svg>
      </div>
      <div class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M19 3V21H15V3H19M14 3V21H10V3H14M9 3V21H5V3H9Z"></path></svg>
      </div>
      <div class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M17,17H7V14L3,18L7,22V19H19V13H17M7,7H17V10L21,6L17,2V5H5V11H7V7Z"></path></svg>
      </div>
    </div>
  </div>
</template>

<script>
import { getCurrentInstance } from 'vue'

export default {
  setup () {
    const { ctx } = getCurrentInstance()

    const test = () => {
      ctx.$mitt.emit('test', '')
    }

    return {
      test
    }
  }
}
</script>

<style lang="stylus" scoped>
.control
  display flex
  flex-direction column
  align-items center
  justify-content center
  position sticky
  bottom 0
  background rgba(255, 255, 255, 0.7)
  .playing
    margin 10px 0
    color rgba(255,0,128,0.5)
  .btn
    display flex
    align-items center
    justify-content center
    margin-bottom 5px
    .icon
      width 30px
      height 30px
      margin 0 5px
      border-radius 50%
      background rgba(255,0,128,0.404)
      cursor pointer
      svg
        height 80%
        width 80%
        padding 10%
        fill #fff
      &:hover
        box-shadow 0px 0px 10px 0px #5bc0de
      &:active
        background rgba(255,0,128,0.5)
</style>
