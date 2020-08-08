import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { createI18n } from 'vue-i18n'
import VoiceList from '../public/translate/voices.json'
import Locales from '../public/translate/locales'

import './assets/style/transition.styl'

const CN = { ...Locales['zh-CN'], voice: {}, voicecategory: {} }
const JP = { ...Locales['ja-JP'], voice: {}, voicecategory: {} }

for (const voiceCategoryList of VoiceList.voices) {
  if (voiceCategoryList.categoryDescription !== undefined) {
    if (voiceCategoryList.categoryDescription['zh-CN'] !== undefined) {
      CN.voicecategory[voiceCategoryList.categoryName] = voiceCategoryList.categoryDescription['zh-CN']
    }
    if (voiceCategoryList.categoryDescription['ja-JP'] !== undefined) {
      JP.voicecategory[voiceCategoryList.categoryName] = voiceCategoryList.categoryDescription['ja-JP']
    }
  }
  for (const voiceItem of voiceCategoryList.voiceList) {
    if (voiceItem.description !== undefined) {
      if (voiceItem.description['zh-CN'] !== undefined) {
        CN.voice[voiceItem.name] = voiceItem.description['zh-CN']
      }
      if (voiceItem.description['ja-JP'] !== undefined) {
        JP.voice[voiceItem.name] = voiceItem.description['ja-JP']
      }
    }
  }
}

const i18n = createI18n({
  legacy: true,
  locale: /ja/i.test(navigator.language) ? 'ja-JP' : 'zh-CN',
  messages: {
    'zh-CN': CN,
    'ja-JP': JP
  }
})

createApp(App).use(router).use(i18n).mount('#app')
