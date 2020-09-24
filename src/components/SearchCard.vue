<template>
  <card class="search-wrapper" :class="{'show-search': isShowSearch}">
    <search class="search" />
  </card>
</template>

<script>
import { inject } from 'vue'
import Search from '@/components/Search.vue'
import Card from '@/components/common/Card.vue'

export default {
  components: {
    Search,
    Card
  },
  setup() {
    const isShowSearch = inject('isShowSearch')

    return {
      isShowSearch
    }
  }
}
</script>

<style lang="stylus" scoped>
.search-wrapper
  // box-sizing border-box
  z-index 1
  position sticky
  top 58px
  height 0
  opacity 0
  margin-top 0
  margin-bottom 0
  transition all 0.3s
  background #fff

  .search
    width 90%
    margin auto

@media only screen and (min-width 550px)
  .search-wrapper
    height 0
    opacity 0
    margin-top 0
    margin-bottom 0

@media only screen and (max-width 550px)
  .show-search
    height 60px
    opacity 1
    margin-top 10px
</style>
