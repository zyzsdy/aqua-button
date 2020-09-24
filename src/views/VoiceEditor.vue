<template>
  <transition name="fade" appear>
    <div class="editor">
      <div class="header">
        <button @click="changeShow">切换至{{ !showCategory ? '分类' : '语音'}}</button>
        <button @click="add">增加{{ showCategory ? '分类' : '语音'}}</button>
        <button @click="dlJson">下载</button>
      </div>
      <table v-if="showCategory">
        <tr>
          <th></th>
          <th>name</th>
          <th>zh-CN</th>
          <th>ja-JP</th>
        </tr>
        <template v-for="(item, index) in data.category" :key="index">
          <tr>
            <td>{{data.category.length - index}}</td>
            <td>
              <input type="text" v-model="item.name" />
            </td>
            <td>
              <input type="text" v-model="item.translate['zh-CN']" />
            </td>
            <td>
              <input type="text" v-model="item.translate['ja-JP']" />
            </td>
          </tr>
        </template>
      </table>
      <table v-else>
        <tr>
          <th></th>
          <th>name</th>
          <th>path</th>
          <th>category</th>
          <th>zh-CN</th>
          <th>ja-JP</th>
        </tr>
        <template v-for="(item, index) in data.voices" :key="item.name">
          <tr>
            <td>{{data.voices.length - index}}</td>
            <td>
              <input type="text" v-model="item.name" />
            </td>
            <td>
              <input type="text" v-model="item.path" />
            </td>
            <td>
              <edit-select :name="item.name" :category="item.category" />
            </td>
            <td>
              <input type="text" v-model="item.translate['zh-CN']" />
            </td>
            <td>
              <input type="text" v-model="item.translate['ja-JP']" />
            </td>
          </tr>
        </template>
      </table>
    </div>
  </transition>
</template>

<script>
import { ref, provide, computed, watch } from 'vue'
import VoiceList from '@/../public/translate/voices.json'
import EditSelect from '@/components/EditSelect.vue'

export default {
  components: {
    EditSelect
  },
  setup() {
    // 是否显示分类
    const showCategory = ref(true)

    const data = ref({
      category: VoiceList.category.reverse(),
      voices: VoiceList.voices.reverse()
    })
    provide('data', data)

    const changeShow = () => {
      showCategory.value = !showCategory.value
    }

    const add = () => {
      if (showCategory.value) {
        data.value.category.unshift({
          name: null,
          translate: {
            'zh-CN': null,
            'ja-JP': null
          }
        })
      } else {
        data.value.voices.unshift({
          name: null,
          path: null,
          translate: {
            'zh-CN': null,
            'ja-JP': null
          },
          category: null
        })
      }
    }

    // 需要定义中间变量才能监听到引用的变化值
    const tempData = computed(() => JSON.parse(JSON.stringify(data.value.category)))

    watch(tempData, (newVal, oldVal) => {
      let oldCategory = null
      let newCategory = null
      for (const i in newVal) {
        const oldIndex = newVal.length - oldVal.length + Number(i)
        if (newVal[i].name !== oldVal[oldIndex].name) {
          oldCategory = oldVal[oldIndex].name
          newCategory = newVal[i].name
          break
        }
      }
      for (const j in data.value.voices) {
        if (data.value.voices[j].category === oldCategory) {
          data.value.voices[j].category = newCategory
        }
      }
    })

    // 下载JSON文件
    const dlJson = () => {
      const jsonData = JSON.stringify(data.value)

      const eleLink = document.createElement('a')
      eleLink.download = 'voices.json'
      eleLink.style.display = 'none'
      // 字符内容转变成blob地址
      const blob = new Blob([jsonData])
      eleLink.href = URL.createObjectURL(blob)
      // 触发点击
      document.body.appendChild(eleLink)
      eleLink.click()
      // 移除DOM
      document.body.removeChild(eleLink)
    }

    return {
      data,
      showCategory,
      changeShow,
      add,
      dlJson
    }
  }
}
</script>

<style lang="stylus" scoped>
table
  max-width 100%

  th
    position sticky
    top 48px
    padding 5px
    background #fff

  td
    text-align center

.editor
  margin 0 10px

  .header
    margin 5px 0 5px 5px
</style>
