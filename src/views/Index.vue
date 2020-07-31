<template>
  <div class="index">
    <live />
    <voice />
  </div>
</template>

<script>
import Live from '../components/Live'
import Voice from '../components/Voice'

export default {
  components: {
    Live,
    Voice
  }
}
</script>

<style lang="stylus" scoped>
.index
  margin 0 auto
  width 90%

@media only screen and (max-width: 600px)
  .index
    width 95%
</style>
