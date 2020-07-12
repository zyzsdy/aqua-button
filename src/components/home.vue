<template>
    <div class="container-fluid">
        <div class="background">
            <img src="../../public/resources/BG2.png" width="100%" height="100%" alt="" />
        </div>
        <div class="top">
            <el-collapse v-model="this.activeNames" @change="this.handleChange">
                <el-collapse-item name="controller">
                    <template slot="title">
                        <i class="el-icon-open titleicon"></i>
                        <p style="font-size:18px">{{$t("action.control")}}</p>
                    </template>
                    <div class="controlgroup">
                    <br/>
                        <el-row>
                            <el-col :span="8">
                            <el-button class="controlbutton" type="primary" @click="random">{{$t("action.randomplay")}}</el-button>
                            </el-col>
                            <el-col :span="8">
                            <el-button class="controlbutton" type="primary" @click="stopPlay">{{$t("action.stopvoice")}}</el-button>
                            </el-col>
                            <el-col :span="8">
                            <el-checkbox style="margin-right:0px" v-model="overlapCheck" @click="overlap" class="checkbox" :class="{'disabled':autoCheck}">{{$t("action.overlap")}}</el-checkbox>
                            </el-col>
                            <el-col :span="8">
                            <el-checkbox style="margin-top:0px" v-model="autoCheck" @click="autoPlay" class="checkbox" :class="{'disabled':overlapCheck}">{{$t("action.autoplay")}}</el-checkbox>
                            </el-col>
                        </el-row>
                    </div>
                    <div class="cate-body" style="margin-top:5px">
                        <span>{{ voice.name ? $t("action.playing") + $t("voice." + voice.name ) : $t("action.noplay") }}</span>
                    </div>
                    <audio id="player" @ended="voiceEnd(false)"></audio>
                </el-collapse-item>
            <br/>
                <el-collapse-item v-for="category in voices" :key="category.categoryName" :name="category.categoryName">
                    <template slot="title">{{ $t("voicecategory." + category.categoryName) }}</template>
                    <el-button class="button" v-for="voiceItem in category.voiceList" v-bind:key="voiceItem.name" @click="play(voiceItem)">
                        {{ $t("voice." + voiceItem.name )}}
                    </el-button>
                </el-collapse-item>          
            </el-collapse>
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
.el-col{
    align-items: center;
    margin-left: auto;
    margin-right: auto;
}
.controlbutton{
    margin-left: auto;
    margin-right: auto;
    display: block;
}
.titleicon{
    margin-right: 20px;
    margin-bottom: 8px;
}
.background{
    z-index: -1;
    position: absolute;
    
    // 平铺
    // width: 100%;
    // height: 100%;
}
.el-collapse{
    background-color: #d777fa;
    opacity: 0.8;
}

.btn-new {
    color: #fff;
    background-color: rgb(38, 176, 211);
    border-color: rgb(211, 38, 211);
    max-width: 100%;
    word-wrap: break-word !important;
    word-break: break-all !important;
    white-space: normal !important;
}
.checkbox {
    display: inline-block;
    vertical-align: middle;
    margin: 0 1px 0 0;
}
</style>


<script>
import Vue from 'vue'
import Component from 'vue-class-component'
import VoiceList from '../voices.json'
@Component
class HomePage extends Vue {
    voices = VoiceList.voices;
    autoCheck = false;
    overlapCheck = false;
    voice = {};
    bgSrc = require('../../public/resources/BG1.jpeg') 
    play(item){
        if (this.overlapCheck) {
            let audio = new Audio("voices/" + item.path);
            this.voice = item;
            audio.play()
        } else {
            this.stopPlay();
            let player = document.getElementById('player');
            player.src = "voices/" + item.path;
            this.voice = item;
            player.play();
        }
    }
    stopPlay(){
        let player = document.getElementById('player');
        player.pause();
        this.voiceEnd(true);
    }
    voiceEnd(flag) {
        if(flag !== true && this.autoCheck) {
            this.random();
        } else {
            this.voice = {};
        }
    }
    random() {
        let tempList = this.voices[this._randomNum(0, this.voices.length - 1)];
        this.play(tempList.voiceList[this._randomNum(0, tempList.voiceList.length - 1)]);
    }
    autoPlay(){
        if (this.overlapCheck) {
            return;
        }
        this.autoCheck = !this.autoCheck;
    }
    overlap() {
        if (this.autoCheck) {
            return;
        }
        this.overlapCheck = !this.overlapCheck;
    }
    _randomNum(minNum, maxNum) {
        switch(arguments.length) {
            case 1:
                return parseInt(Math.random() * minNum + 1, 10);
            case 2:
                return parseInt(Math.random() * (maxNum - minNum + 1) + minNum, 10);
            default:
                return 0;
        }
    }
    activeNames = ['controller','lmao','regigigas'];
    handleChange(val){
            console.log(val)
        }
}
export default HomePage;
</script>
