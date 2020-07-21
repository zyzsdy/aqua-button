<template>
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                    <h4 class="modal-title" id="myModalLabel">{{$t(title)}}</h4>
                </div>
                <div class="modal-body">
                    {{$t(msg)}}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">{{$t("action.close")}}</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss">
.modal{
    color: black;
}
</style>


<script>
import Vue from 'vue'
import Component from 'vue-class-component'
import $ from 'jquery'

@Component
class Modal extends Vue {
    title = "info.info";
    msg = "info.null";
    created(){
        this.$gConst.globalbus.$on("send-info", (info) => {
            this.msg = info;
            this.showModal();
        });
    }
    showModal(){
        $("#myModal").modal();
    }
}
export default Modal;
</script>
