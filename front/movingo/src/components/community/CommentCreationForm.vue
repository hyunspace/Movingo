<template>
  <div id="comment-creation-form" class="row">
    <input class="col-10" id="comment-creation-content" v-model="newcomment.content" type="text">
    <form @submit.prevent="submit(threadPk)" style="margin:0; padding-right:0;" class="col-2">
      <button id="comment-creation-btn">작성</button>
    </form>
    
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: "CommentCreationForm",
  props: {
    threadPk: Number,
  },
  data() {
    return {
      newcomment:{
        content: "",
      }
    }

  },
  methods: {
    ...mapActions(['createComment']),
    submit(){
      let data = {
        threadPk: this.threadPk,
        newcomment:this.newcomment
      }
      this.createComment(data)
      this.newcomment.content = ""
    }
  }
}
</script>

<style scoped>
#comment-creation-content{
  height:35px;
  border-radius: 7px;
  border: transparent;
}
#comment-creation-btn{
  height:36px;
  border: transparent;
  border-radius: 7px;
  background: #e11616;
  color: #ffffff;
  margin:0;
  width:100%
}
</style>