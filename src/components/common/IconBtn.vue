<template>
  <a :href="url" class="icon" target="_blank">
    <img draggable="false" :src="img" />
  </a>
</template>

<script>
export default {
  props: {
    url: {
      type: String
    },
    img: {
      type: String
    }
  }
}
</script>

<style lang="stylus" scoped>
.icon
  width 30px
  height 30px
  margin 0 5px
  border-radius 50%
  background rgba(255, 255, 255, 0.5)

  img
    height 80%
    padding 10%

  &:hover
    box-shadow 0px 0px 10px 0px $sub-color

    img
      height 90%
      padding 5%

  &:active
    background rgba(255, 255, 255, 0.6)

    img
      height 80%
      padding 10%
</style>
