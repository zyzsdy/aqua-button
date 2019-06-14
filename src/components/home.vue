<template>
    <div class="container-fluid" >
        <div>
            <div class="cate-header">{{ $t("action.control")}}</div>
            <div class="cate-body"><button class="btn btn-info" @click="stopPlay">{{$t("action.stopvoice")}}</button></div>
            <audio id="player"></audio>
        </div>
        <div v-for="category in voices" v-bind:key="category.categoryName">
            <div class="cate-header">{{ $t("voicecategory." + category.categoryName) }}</div>
            <div class="cate-body">
                <button class="btn btn-new" v-for="voiceItem in category.voiceList" v-bind:key="voiceItem.name" @click="play(voiceItem.path)">
                    {{ $t("voice." + voiceItem.name )}}
                </button>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.cate-header{
    background-color: rgba(255, 0, 128, 0.404);
    border: 1px solid rgba(0, 0, 0, 0.5);
    border-radius: 10px;
    text-align: center;
    font-size: 20px;
    margin-bottom: 12px;
}
.cate-body{
    margin-bottom: 12px;
    text-align: center;
}
.cate-body button{
    margin: 5px;
}
.btn-new {
    color: #fff;
    background-color: rgb(38, 176, 211);
    border-color: rgb(211, 38, 211);
}
</style>


<script>
import Vue from 'vue'
import Component from 'vue-class-component'
import VoiceList from '../voices.json'

@Component
class HomePage extends Vue {
    voices = VoiceList.voices
    play(path){
        this.stopPlay();
        let player = document.getElementById('player');
        player.src = "voices/" + path;
        player.play();
    }
    stopPlay(){
        let player = document.getElementById('player');
        player.pause();
    }
}
export default HomePage;
</script>