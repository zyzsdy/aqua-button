<template>
  <div class="live-wrapper">
    <card>
      <template v-slot:header>
        <div class="title">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="24" width="24" role="img" aria-hidden="true"><path d="M12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22C6.47,22 2,17.5 2,12A10,10 0 0,1 12,2M12.5,7V12.25L17,14.92L16.25,16.15L11,13V7H12.5Z"></path></svg>
          <div>直播动态</div>
        </div>
      </template>
      <div class="content">
        <p>直播动态尚未完成</p>
        <p>播放功能尚未完成</p>
      </div>
    </card>
  </div>
</template>

<script>
import Card from './common/Card'

export default {
  components: {
    Card
  }
}
</script>

<style lang="stylus" scoped>
.live-wrapper
  margin 10px auto
  .title
    display flex
    align-items center
    height 40px
    margin-left 10px
    div
      font-size 20px
      margin-left 10px
    svg
      fill rgba(255,0,128,.404)
  .content
    padding 10px
</style>
