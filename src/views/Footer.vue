<template>
  <transition name="fade" appear>
    <div class="footer">
      <div>
        <div class="author">
          <div>©2020</div>
          <template v-for="(item, index) in author" :key="index">
            <a v-if="index > 0">&</a>
            <a :href="item.url || null" target="_blank">{{item.name}}</a>
          </template>
        </div>
        <div class="info">
          <template v-for="(item, index) in info" :key="index">
            <div v-html="item"></div>
          </template>
        </div>
      </div>
      <div class="text-right">
        <div class="git">
          <i-btn class="btn" :url="githubUrl" :img="require('../assets/image/github-fill.png')" />
          <a :href="githubUrl" target="_blank">{{ t(INFO_I18N.toGithub) }}</a>
        </div>
        <div>{{ t(INFO_I18N.notOfficial) }}</div>
      </div>
    </div>
  </transition>
</template>

<script>
import { useI18n } from 'vue-i18n'
import { INFO_I18N } from '@/assets/script/option'
import IBtn from '@/components/common/IconBtn'
import Setting from '@/../public/setting/setting.json'

export default {
  components: {
    IBtn
  },
  setup() {
    const { t } = useI18n()

    return {
      INFO_I18N,
      t,
      author: Setting.footer && Setting.footer.author ? Setting.footer.author : [],
      info: Setting.footer && Setting.footer.info ? Setting.footer.info : [],
      githubUrl: Setting.footer && Setting.footer.githubUrl ? Setting.footer.githubUrl : null
    }
  }
}
</script>

<style lang="stylus" scoped>
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

  .info
    margin-top 5px
    line-height 18px

  .text-right
    text-align right

    .git
      display flex
      align-items center

      a
        margin 0

      .btn
        margin 0 5px

@media only screen and (max-width 600px)
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
