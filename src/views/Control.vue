<template>
  <transition name="slider-up" appear>
    <div class="control">
      <div class="playing">
        <transition name="fade">
          <loading v-if="playSetting.nowPlay && playSetting.loading" class="tip" />
        </transition>
        <transition name="fade-delay">
          <error v-if="playSetting.nowPlay && playSetting.error" class="tip" />
        </transition>
        <div :style="{'text-decoration': isError}">{{ title }}</div>
      </div>
      <div class="btn">
        <div class="icon" :title="t(ACTION_I18N.randomplay)" @click="randomPlay">
          <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" width="24" height="24">
            <path
              d="M689.066667 170.666667c-40.533333 0-132.266667 19.2-177.066667 119.466666C467.2 189.866667 377.6 170.666667 334.933333 170.666667 211.2 170.666667 128 266.666667 128 373.333333 128 631.466667 512 853.333333 512 853.333333s384-221.866667 384-480c0-106.666667-83.2-202.666667-206.933333-202.666666z"
            />
          </svg>
        </div>
        <div class="icon" :title="t(ACTION_I18N.stopvoice)" @click="stopPlay">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            height="24"
            width="24"
            role="img"
            aria-hidden="true"
          >
            <path d="M18,18H6V6H18V18Z" />
          </svg>
        </div>
        <div
          class="icon"
          :title="t(ACTION_I18N.overlap)"
          @click="overlapChange"
          :class="{'icon-active': playSetting.overlap}"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            height="24"
            width="24"
            role="img"
            aria-hidden="true"
          >
            <path d="M19 3V21H15V3H19M14 3V21H10V3H14M9 3V21H5V3H9Z" />
          </svg>
        </div>
        <div
          class="icon"
          :title="t(ACTION_I18N.autoRandom)"
          @click="autoRandomChange"
          :class="{'icon-active': playSetting.autoRandom}"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            height="24"
            width="24"
            role="img"
            aria-hidden="true"
          >
            <path
              d="M14.83,13.41L13.42,14.82L16.55,17.95L14.5,20H20V14.5L17.96,16.54L14.83,13.41M14.5,4L16.54,6.04L4,18.59L5.41,20L17.96,7.46L20,9.5V4M10.59,9.17L5.41,4L4,5.41L9.17,10.58L10.59,9.17Z"
            />
          </svg>
        </div>
        <div
          class="icon"
          :title="t(ACTION_I18N.loop)"
          @click="loopChange"
          :class="{'icon-active': playSetting.loop}"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            height="24"
            width="24"
            role="img"
            aria-hidden="true"
          >
            <path d="M17,17H7V14L3,18L7,22V19H19V13H17M7,7H17V10L21,6L17,2V5H5V11H7V7Z" />
          </svg>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { inject, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { ACTION_I18N, EVENT } from '@/assets/script/option'
import mitt from '@/assets/script/mitt'
import Loading from '@/components/common/Loading'
import Error from '@/components/common/Error'

export default {
  components: {
    Loading,
    Error
  },
  setup() {
    const { t } = useI18n()
    const playSetting = inject('playSetting')

    // 控制栏文字显示
    const title = computed(() => {
      if (playSetting.overlap) {
        return t(ACTION_I18N.overlapTip)
      } else if (playSetting.nowPlay) {
        return t('voice.' + playSetting.nowPlay.name)
      } else if (playSetting.autoRandom) {
        return t(ACTION_I18N.autoRandomTip)
      } else if (playSetting.loop) {
        return t(ACTION_I18N.loopTip)
      } else {
        return t(ACTION_I18N.noplay)
      }
    })

    const isError = computed(() => {
      return playSetting.error ? 'line-through' : 'none'
    })

    const randomPlay = () => {
      mitt.emit(EVENT.randomPlay)
    }

    const stopPlay = () => {
      mitt.emit(EVENT.stopPlay)
    }

    const overlapChange = () => {
      playSetting.autoRandom = false
      playSetting.loop = false
      playSetting.overlap = !playSetting.overlap
    }

    const autoRandomChange = () => {
      playSetting.overlap = false
      playSetting.loop = false
      playSetting.autoRandom = !playSetting.autoRandom
    }

    const loopChange = () => {
      playSetting.overlap = false
      playSetting.autoRandom = false
      playSetting.loop = !playSetting.loop
    }

    return {
      ACTION_I18N,
      t,
      isError,
      title,
      playSetting,
      randomPlay,
      stopPlay,
      overlapChange,
      autoRandomChange,
      loopChange
    }
  }
}
</script>

<style lang="stylus" scoped>
.control
  display flex
  flex-direction column
  align-items center
  justify-content center
  position sticky
  bottom 0
  background rgba(255, 255, 255, 0.7)

  .playing
    position relative
    margin 10px 0
    max-width 80%
    line-height 21px
    text-align center
    color $title-color

    .tip
      position absolute
      left -23px
      top 0
      height 100%

  .btn
    display flex
    align-items center
    justify-content center
    margin-bottom 10px

    .icon
      width 30px
      height 30px
      margin 0 5px
      border-radius 50%
      background $main-color
      cursor pointer

      svg
        height 80%
        width 80%
        padding 10%
        fill #fff

      &:hover
        box-shadow 0px 0px 10px 0px $sub-color

      &:active
        background $title-color

    .icon-active
      background $sub-color
</style>
