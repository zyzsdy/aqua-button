import Vue from 'vue'
import Router from 'vue-router'

import HomePage from './components/home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {path: '/', name: "home", component: HomePage},
  ]
})
