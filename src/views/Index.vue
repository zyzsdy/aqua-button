<template>
  <div class="index">
    <live />
    <voice />
    <card>
      <div
        style="text-align: center"
      >{{ t(INFO_I18N.voiceTotalTip) }}: {{ t(INFO_I18N.voiceTotal) }}</div>
    </card>
    <card style="display: flex;justify-content: center">
      <a href="https://vtbbtn.org/" target="_blank">{{ t(INFO_I18N.vtbbtn) }}</a>
    </card>
  </div>
</template>

<script>
import { useI18n } from 'vue-i18n'
import { INFO_I18N } from '@/assets/script/option'
import Live from '@/components/Live'
import Voice from '@/components/Voice'
import Card from '@/components/common/Card'

export default {
  components: {
    Live,
    Voice,
    Card
  },
  setup() {
    const { t } = useI18n()

    return {
      t,
      INFO_I18N
    }
  }
}
</script>

<style lang="stylus" scoped>
a
  margin 0 5px

.index
  margin 0 auto
  width 90%

@media only screen and (max-width 600px)
  .index
    width 95%
</style>
