<template>
  <div>
    <template v-for="item in voices">
      <card :key="item.categoryName">
        <template v-slot:header>
          <div class="category">{{ $t("voicecategory." + item.categoryName) }}</div>
        </template>
        <div class="content">
          <template v-for="voice in item.voiceList">
            <v-btn :key="voice.name" :text="$t('voice.' + voice.name)" />
          </template>
        </div>
      </card>
    </template>
  </div>
</template>

<script>
import VoiceList from '../voices.json'
import { ref } from 'vue'
import Card from './common/Card'
import VBtn from './common/VoiveBtn'

export default {
  components: {
    Card,
    VBtn
  },
  setup () {
    const voices = VoiceList.voices
    const voive = ref({})

    return {
      voices,
      voive
    }
  }
}
</script>

<style lang="stylus" scoped>
.category
  font-size 24px
  padding 14px 10px
.content
  display flex
  flex-wrap wrap
</style>
