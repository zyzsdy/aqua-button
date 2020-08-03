<template>
  <div>
    <template v-for="item in voices">
      <card :key="item.categoryName">
        <template v-slot:header>
          <div class="category">{{ $t("voicecategory." + item.categoryName) }}</div>
        </template>
        <div class="content">
          <template v-for="voice in item.voiceList">
            <v-btn :key="voice.name" :text="$t('voice.' + voice.name)" :playing="overlapShowList.includes(voice.name)" :progress="setting && setting.nowPlay && setting.nowPlay.name === voice.name ? progress : 0" @click="play(voice)" />
          </template>
        </div>
      </card>
    </template>
    <audio ref="voice" @canplay="canPlay" @timeupdate="timeUpdate" @ended="voiceEnd"></audio>
  </div>
</template>

<script>
import VoiceList from '../voices.json'
import { reactive, inject, onMounted, getCurrentInstance, computed, ref } from 'vue'
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
    const setting = inject('setting')

    const voices = VoiceList.voices
    let player = null
    const overlapPlayList = {}
    const overlapShowList = reactive([])

    onMounted(() => {
      player = ctx.$refs.voice
    })

    const play = (data) => {
      if (!setting.overlap) {
        player.pause()
        player.src = 'voices/' + data.path
        setting.nowPlay = data
        player.play()
      } else {
        const key = new Date().getTime()
        overlapShowList.push(data.name)
        overlapPlayList[key] = new Audio('voices/' + data.path)
        overlapPlayList[key].addEventListener('ended', () => {
          delete overlapPlayList[key]
          if (overlapShowList.includes(data.name)) {
            overlapShowList.splice(overlapShowList.indexOf(data.name), 1)
          }
        }, {
          capture: false,
          passive: false,
          once: true
        })
        overlapPlayList[key].play()
      }
    }

    const duration = ref(0)
    const currentTime = ref(0)

    const canPlay = (e) => {
      duration.value = e.target.duration
    }

    const timeUpdate = (e) => {
      currentTime.value = e.target.currentTime
    }

    const progress = computed(() => {
      return (currentTime.value / duration.value) * 100
    })

    const voiceEnd = () => {
      duration.value = 0
      currentTime.value = 0
      if (setting.autoRandom) {
        randomPlay()
        return
      }
      if (setting.loop) {
        play(setting.nowPlay)
        return
      }
      setting.nowPlay = null
    }

    mitt.on('randomPlay', () => {
      randomPlay()
    })

    const randomPlay = () => {
      const tempList = voices[_getrRandomInt(voices.length - 1)]
      play(tempList.voiceList[_getrRandomInt(tempList.voiceList.length - 1)])
    }

    mitt.on('stopPlay', () => {
      for (const key in overlapPlayList) {
        overlapPlayList[key].pause()
        delete overlapPlayList[key]
      }
      overlapShowList.length = 0
      player.pause()
      voiceEnd()
    })

    const _getrRandomInt = (max) => {
      return Math.floor(Math.random() * Math.floor(max))
    }

    return {
      setting,
      overlapShowList,
      voices,
      play,
      canPlay,
      timeUpdate,
      progress,
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
