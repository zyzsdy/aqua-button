<template>
  <transition name="fade" appear>
    <div>
      <search class="search" />
      <div v-for="item in voices" :key="item.name">
        <card v-if="needToShow(item.translate)">
          <template v-slot:header>
            <div class="category">{{ t('voicecategory.' + item.name) }}</div>
          </template>
          <div class="content">
            <div v-for="voice in item.voiceList" :key="voice.name">
              <div v-if="needToShow(voice.translate)" class="btn-wrapper">
                <v-btn
                  :text="t('voice.' + voice.name)"
                  class="v-btn"
                  :class="{ 'search-list': searchList.length > 0 && !searchList.includes(voice.name), 'highlight': highlight === voice.name }"
                  :name="voice.name"
                  @click="play(voice)"
                  :ref="el => { el ? btnList[voice.name] = el : null }"
                />
                <img
                  class="pic"
                  v-if="needUsePicture(voice.usePicture)"
                  :src="usePicture(voice.usePicture)"
                />
              </div>
            </div>
          </div>
        </card>
      </div>
    </div>
  </transition>
</template>

<script>
import { ref, reactive, provide, inject, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { EVENT, INFO_I18N } from '@/assets/script/option'
import mitt from '@/assets/script/mitt'
import VoiceList from '@/../public/translate/voices.json'
import Setting from '@/../public/setting/setting.json'
import Card from './common/Card.vue'
import VBtn from './common/VoiveBtn.vue'
import Search from '@/components/SearchCard.vue'

export default {
  components: {
    Card,
    VBtn,
    Search
  },
  setup() {
    const { t, locale } = useI18n()

    // 判断浏览器是否为夸克从而停用部分功能
    const isQuark = navigator.userAgent.toLowerCase().includes('quark')

    const playSetting = inject('playSetting')

    // 所有按钮的引用
    const btnList = ref({})

    const searchData = inject('searchData')
    const highlight = ref('')

    mitt.on(EVENT.autoScroll, () => {
      if (searchData.list && searchData.list.length > 0) {
        for (const i in btnList.value) {
          if (searchData.index + 1 > searchData.list.length) searchData.index = 0
          if (i === searchData.list[searchData.index]) {
            searchData.index++
            const scrollPos = document.documentElement.scrollTop + btnList.value[i].$el.getBoundingClientRect().top - 200
            highlight.value = i
            window.scrollTo({ top: scrollPos, behavior: 'smooth' })
            break
          }
        }
      }
    })

    watch(() => {
      return searchData.value
    }, () => {
      highlight.value = ''
    })

    const voices = reactive([])
    VoiceList.category.forEach(category => {
      const temp = { ...category, voiceList: [] }
      VoiceList.voices.forEach(voice => {
        if (voice.category === category.name) {
          temp.voiceList.push(voice)
        }
      })
      voices.push(temp)
    })
    provide('voices', voices)

    if ('mediaSession' in navigator) {
      navigator.mediaSession.setActionHandler('nexttrack', () => {
        randomPlay()
      })
      navigator.mediaSession.setActionHandler('previoustrack', () => {
        randomPlay()
      })
      navigator.mediaSession.setActionHandler('pause', () => {
        if (playerList.has('once')) playerList.get('once').audio.pause()
        navigator.mediaSession.playbackState = 'paused'
      })
    }

    let timer = null

    /**
     * 重置播放状态
     */
    const reset = () => {
      playSetting.loading = true
      playSetting.nowPlay = null
      playSetting.error = false
    }

    const playerList = new Map()

    /**
     * @param voice 语音对象
     * @param category 所属分类的name
     */
    const play = (voice) => {
      if (!playSetting.overlap) {
        if (playerList.has('once')) playerList.get('once').audio.pause()
        if (playSetting.nowPlay && playSetting.nowPlay.name === voice.name) {
          clearTimeout(timer)
          playerList.get('once').audio.currentTime = 0
          playerList.get('once').audio.pause()
          timer = setTimeout(() => {
            playerList.get('once').audio.play()
          }, 250)
        } else {
          addPlayer(voice, 'once')

          if ('mediaSession' in navigator) {
            const meta = {
              title: t('voice.' + voice.name),
              artist: t(INFO_I18N.fullName),
              album: t(INFO_I18N.title),
              artwork: [{ src: `/other/${Setting.mediaSession.artwork}`, sizes: '128x128' }]
            }
            navigator.mediaSession.metadata = new window.MediaMetadata(meta)
            navigator.mediaSession.playbackState = 'playing'
          }
        }
      } else {
        const key = new Date().getTime()
        addPlayer(voice, key)
      }
    }

    /**
     * 把语音对象添加到MAP
     */
    const addPlayer = (voice, key) => {
      reset()
      playerList.set(key, {
        name: voice.name,
        audio: new Audio(`voices/${voice.path}`)
      })
      if (!playSetting.overlap) playSetting.nowPlay = voice
      playerList.get(key).audio.play()
      playerList.get(key).audio.onerror = () => {
        playSetting.loading = false
        playSetting.error = true
      }
      playerList.get(key).audio.oncanplay = () => {
        if (playSetting.overlap) {
          for (const i of playerList.keys()) {
            if (playerList.get(i).name === voice.name) {
              playerList.get(i).audio.ontimeupdate = null
              playerList.get(i).audio.onended = () => {
                playerList.delete(i)
              }
            }
          }
        }
        playSetting.loading = false
        // eslint-disable-next-line no-labels
        voices:
        for (const i in voices) {
          for (const j in voices[i].voiceList) {
            if (voices[i].voiceList[j].name === voice.name) {
              playerList.get(key).voicesKey = [i, j]
              const duration = playerList.get(key).audio.duration
              let currentTime = 0
              playerList.get(key).audio.ontimeupdate = () => {
                currentTime = Number(((playerList.get(key).audio.currentTime / duration) * 100).toFixed(0))
                if (isQuark) {
                  if (currentTime !== 0) {
                    voices[i].voiceList[j].progress = 100
                  } else {
                    voices[i].voiceList[j].progress = 0
                  }
                } else {
                  voices[i].voiceList[j].progress = currentTime
                }
              }
              playerList.get(key).audio.onended = () => {
                voices[i].voiceList[j].progress = 0
                if (playSetting.loop) {
                  play(voice)
                } else {
                  reset()
                  playerList.delete(key)
                }
                if (playSetting.autoRandom) {
                  randomPlay()
                }
              }
              // eslint-disable-next-line no-labels
              break voices
            }
          }
        }
      }
    }

    mitt.on(EVENT.randomPlay, () => {
      randomPlay()
    })

    /**
     * 随机播放失败次数
     */
    let errTimes = 0

    /**
     * 随机播放
     */
    const randomPlay = () => {
      const randomList = voices[_getrRandomInt(voices.length - 1)]
      const randomVoice = randomList.voiceList[_getrRandomInt(randomList.voiceList.length - 1)]
      if (needToShow(randomList.translate) && needToShow(randomVoice.translate)) {
        errTimes = 0
        play(randomVoice)
      } else if (errTimes <= 5) {
        ++errTimes
        randomPlay()
        // 连续五次不存在停止随机
      }
    }

    mitt.on(EVENT.stopPlay, () => {
      clearTimeout(timer)
      for (const key of playerList.keys()) {
        playerList.get(key).audio.pause()
        playerList.get(key).audio.onerror = null
        playerList.get(key).audio.oncanplay = null
        playerList.get(key).audio.ontimeupdate = null
        playerList.get(key).audio.onended = null
        const voicesKey = playerList.get(key).voicesKey
        if (voicesKey) {
          voices[voicesKey[0]].voiceList[voicesKey[1]].progress = 0
        }
      }
      playerList.clear()
      reset()
    })

    /**
     * 返回需要显示的表情包url
     */
    const usePicture = (name) => {
      if (name) {
        const lang = locale.value
        return `/voices/img/${name[lang]}`
      }
    }

    /**
     * 判断是否使用表情包
     */
    const needUsePicture = (usePicture) => {
      if (usePicture) {
        return locale.value in usePicture
      } else {
        return false
      }
    }

    /**
     * 判断是否需要显示
     */
    const needToShow = (translate) => {
      return locale.value in translate
    }

    /**
     * 获取随机数
     */
    const _getrRandomInt = (max) => {
      return Math.floor(Math.random() * Math.floor(max))
    }

    return {
      t,
      btnList,
      searchList: searchData.list,
      highlight,
      voices,
      play,
      usePicture,
      needUsePicture,
      needToShow
    }
  }
}

</script>
<style lang="stylus" scoped>
.search-list
  background #ccc

.highlight
  background $active-color

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

    .v-btn
      transition background 0.2s

    .pic
      position absolute
      bottom calc(100% + 10px)
      left 50%
      width 120%
      min-width 100px
      max-width 200px
      opacity 0
      transform translateX(-50%)
      pointer-events none

@media only screen and (min-width 600px)
  .btn-wrapper
    .pic
      transition opacity 0.5s

    &:hover
      .pic
        opacity 1
        box-shadow 0px 5px 10px 0px $main-color

@media only screen and (max-width 600px)
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
