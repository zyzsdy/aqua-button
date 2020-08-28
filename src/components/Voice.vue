<template>
  <div>
    <div v-for="item in voices" :key="item.categoryName">
      <card v-if="_needToShow(item.categoryDescription)">
        <template v-slot:header>
          <div class="category">{{ $t("voicecategory." + item.categoryName) }}</div>
        </template>
        <div class="content">
          <div v-for="voice in item.voiceList" :key="voice.name">
            <div v-if="_needToShow(voice.description)" class="btn-wrapper">
              <v-btn :text="$t('voice.' + voice.name)" :playing="overlapShowList.includes(voice.name)" :progress="setting && setting.nowPlay && setting.nowPlay.name === voice.name ? progress : 0" @click="play(voice, item.name)" />
              <img class="pic" v-if="_needUsePicture(voice.usePicture)" :src="usePicture(voice.usePicture)">
            </div>
          </div>
        </div>
      </card>
    </div>
    <card>
      <div style="text-align: center">{{ $t('voiceTotalTip') }}: {{ $t('voiceTotal') }}</div>
    </card>
    <audio ref="player" @ended="voiceEnd" @canplay="canplay" @error="error"></audio>
  </div>
</template>

<script>
import { reactive, inject, ref, getCurrentInstance, computed } from 'vue'
import VoiceList from '../../public/translate/voices.json'
import { other } from '../../public/translate/locales'
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
    const isQuark = navigator.userAgent.toLowerCase().includes('quark')

    const setting = inject('setting')

    const voices = VoiceList.voices
    const overlapPlayList = {}
    const overlapShowList = reactive([])

    const player = ref(null)

    let timeout = null
    let interval = null

    const reset = () => {
      if (isQuark) {
        overlapShowList.length = 0
      } else {
        resetInterval()
        currentTime.value = 0
        duration.value = 0
      }
      setting.loading = true
      setting.nowPlay = null
      setting.error = false
    }

    const resetInterval = () => {
      if (interval) {
        clearInterval(interval)
        interval = null
      }
    }

    const play = (data) => {
      if (!setting.overlap) {
        player.value.pause()
        resetInterval()
        if (setting.nowPlay && setting.nowPlay.name === data.name) {
          player.value.currentTime = 0
          player.value.pause()
          timeout = setTimeout(() => {
            player.value.play()
          }, 350)
        } else {
          if (setting.nowPlay) {
            reset()
          }
          if (isQuark) {
            overlapShowList.push(data.name)
          }
          player.value.src = `voices/${data.path}`
          setting.nowPlay = data
          player.value.play()

          if ('mediaSession' in navigator) {
            const meta = {
              title: ctx.$t('voice.' + data.name),
              artist: ctx.$t('info.fullName'),
              album: ctx.$t('info.title'),
              artwork: [{ src: `/image/${other.artwork}`, sizes: '128x128' }]
            }
            navigator.mediaSession.metadata = new window.MediaMetadata(meta)
          }
        }
      } else {
        const key = new Date().getTime()
        overlapShowList.push(data.name)
        overlapPlayList[key] = new Audio(`voices/${data.path}`)
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

    const progress = computed(() => {
      const num = Number(((currentTime.value / duration.value) * 100).toFixed(0))
      if (num !== Infinity && !isNaN(num)) {
        return num
      } else {
        return 0
      }
    })

    const canplay = (e) => {
      setting.loading = false
      if (!isQuark) {
        duration.value = e.target.duration
        interval = setInterval(() => {
          if (e) {
            currentTime.value = e.target.currentTime
          } else {
            resetInterval()
          }
        }, 100)
      }
    }

    const error = () => {
      setting.loading = false
      setting.error = true
    }

    const voiceEnd = () => {
      resetInterval()
      currentTime.value = duration.value
      if (setting.loop) {
        play(setting.nowPlay)
        return
      }
      reset()
      if (setting.autoRandom) {
        randomPlay()
      }
    }

    mitt.on('randomPlay', () => {
      randomPlay()
    })

    let errTimes = 0

    const randomPlay = () => {
      const randomList = voices[_getrRandomInt(voices.length - 1)]
      const randomVoice = randomList.voiceList[_getrRandomInt(randomList.voiceList.length - 1)]
      if (_needToShow(randomList.categoryDescription) && _needToShow(randomVoice.description)) {
        errTimes = 0
        play(randomVoice)
      } else if (errTimes >= 5) {
        // 连续五次不存在停止随机
      } else {
        ++errTimes
        randomPlay()
      }
    }

    mitt.on('stopPlay', () => {
      for (const key in overlapPlayList) {
        overlapPlayList[key].pause()
        delete overlapPlayList[key]
      }
      overlapShowList.length = 0
      if (timeout) {
        clearTimeout(timeout)
        timeout = null
      }
      reset()
      player.value.pause()
    })

    const usePicture = (name) => {
      const locale = ctx.$i18n.locale
      return `/voices/${name[locale]}`
    }

    const _needUsePicture = (usePicture) => {
      if (usePicture) {
        const locale = ctx.$i18n.locale
        return usePicture[locale] !== undefined
      } else {
        return false
      }
    }

    const _getrRandomInt = (max) => {
      return Math.floor(Math.random() * Math.floor(max))
    }

    const _needToShow = (description) => {
      const locale = ctx.$i18n.locale
      return description[locale] !== undefined
    }

    return {
      setting,
      player,
      overlapShowList,
      voices,
      play,
      progress,
      canplay,
      error,
      voiceEnd,
      usePicture,
      _needUsePicture,
      _needToShow
    }
  }
}

</script>
<style lang="stylus" scoped>
@import '~@/assets/style/base.styl'

.category
  font-size 24px
  padding 14px 10px
  user-select none
.content
  display flex
  flex-wrap wrap
  .btn-wrapper
    position relative
    margin 5px
    .pic
      position absolute
      bottom calc(100% + 10px)
      left 50%
      width 120%
      max-width 200px
      opacity 0
      transform translateX(-50%)
      pointer-events none

@media only screen and (min-width: 600px)
  .btn-wrapper
    .pic
      transition opacity 0.5s
    &:hover
      .pic
        opacity 1
        box-shadow 0px 5px 10px 0px $main-color
@media only screen and (max-width: 600px)
  .btn-wrapper
    .pic
      transition opacity 0.5s
      transition-delay 1.5s
    &:active
      .pic
        opacity 1
        transition opacity 0s
        transition-delay 0s

</style>
