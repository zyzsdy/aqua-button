<template>
  <div>
    <template v-for="item in voices">
      <card :key="item.categoryName">
        <template v-slot:header>
          <div class="category">{{ $t("voicecategory." + item.categoryName) }}</div>
        </template>
        <div class="content">
          <template v-for="voice in item.voiceList">
            <v-btn :key="voice.name" :text="$t('voice.' + voice.name)" @click="play(voice)" />
          </template>
        </div>
      </card>
    </template>
    <audio ref="voice" @ended="voiceEnd"></audio>
  </div>
</template>

<script>
import VoiceList from '../voices.json'
import { ref, onMounted, getCurrentInstance } from 'vue'
import Card from './common/Card'
import VBtn from './common/VoiveBtn'
import mitt from '../assets/js/mitt'

export default {
  components: {
    Card,
    VBtn
  },
  setup () {
    const { ctx } = getCurrentInstance()

    const voices = VoiceList.voices
    const nowPlay = ref(null)

    let player = null

    onMounted(() => {
      player = ctx.$refs.voice
    })

    const play = (data) => {
      if (!overlap.value && nowPlay.value) {
        player.pause()
      }
      player.src = 'voices/' + data.path
      nowPlay.value = data
      mitt.emit('nowPlay', ctx.$t('voice.' + data.name))
      player.play()
    }

    const voiceEnd = () => {
      if (autoRandom.value) {
        randomPlay()
        return
      }
      if (loop.value) {
        play(nowPlay.value)
        return
      }
      nowPlay.value = null
      mitt.emit('nowPlay', null)
    }

    mitt.on('randomPlay', () => {
      randomPlay()
    })

    const randomPlay = () => {
      const tempList = voices[_getrRandomInt(voices.length - 1)]
      play(tempList.voiceList[_getrRandomInt(tempList.voiceList.length - 1)])
    }

    mitt.on('stopPlay', () => {
      player.pause()
      voiceEnd()
    })

    const overlap = ref(false)
    const autoRandom = ref(false)
    const loop = ref(false)

    mitt.on('setting', setting => {
      overlap.value = setting.overlap
      autoRandom.value = setting.autoRandom
      loop.value = setting.loop
    })

    const _getrRandomInt = (max) => {
      return Math.floor(Math.random() * Math.floor(max))
    }

    return {
      voices,
      nowPlay,
      play,
      voiceEnd
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
