import Vue from 'vue'

class GlobalConst{
    install(vue){
        vue.prototype.$gConst = {
            globalbus: new Vue()
        }
    }
}
export default new GlobalConst();