<template>
  <div class="card-wrapper">
    <div class="card-header" v-if="$slots.header">
      <slot name="header"></slot>
    </div>
    <div class="card-text">
      <slot></slot>
    </div>
  </div>
</template>

<style lang="stylus" rel="stylesheet/stylus" scoped>
.card-wrapper
  margin 10px 5px
  border-radius 5px
  border 1px solid #EBEEF5
  background-color #FFF
  overflow hidden
  color #303133
  transition box-shadow 0.25s
  &:hover
    box-shadow 2px 2px 5px rgba(0, 0, 0, 0.1)
  .card-header
    border-bottom 1px solid #EBEEF5
    padding 5px
  .card-text
    padding 15px 10px
</style>
