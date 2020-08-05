<template>
  <div class="footer">
    <div class="author">
      <div>©2019-2020</div>
      <a href="https://github.com/zyzsdy" target="_blank">Zyzsdy</a>
      <a href="https://github.com/blacktunes" target="_blank">Blacktunes</a>
    </div>
    <div class="text-right">
      <div class="git">
        <i-btn class="btn" :url="githubUrl" :img="require('../assets/image/github-fill.svg')" />
        <a :href="githubUrl" target="_blank">
          {{$t("info.toGithub")}}
        </a>
      </div>
      <div>{{$t("info.notOfficial")}}</div>
    </div>
  </div>
</template>

<script>
import IBtn from '../components/common/IconBtn'

export default {
  components: {
    IBtn
  },
  data () {
    return {
      githubUrl: 'https://github.com/blacktunes/aqua-button'
    }
  }
}
</script>

<style lang="stylus" scoped>
a
  margin-left 5px
  color #888
  text-decoration none

.footer
  display flex
  justify-content space-between
  flex-wrap wrap
  padding 5px
  background-color #ebebeb
  font-size 12px
  color #333
  .author
    display flex
    align-items center
  .text-right
    text-align right
    .git
      display flex
      align-items center
      a
        margin 0
      .btn
        margin 0 5px

@media only screen and (max-width: 600px)
  .footer
    flex-direction column
    .text-right
      text-align left
      .git
        display flex
        align-items center
        .btn
          order 10
</style>
