<template>
  <div id="thread-detail">
    <h2>{{ title }}</h2>
    <div id="thread-content" class="d-flex justify-content-between">
      <div id="thread-poster">
        <img style="width:100%; border-radius:10px;" :src="thread_poster_path" alt="">  
      </div>
      <div id="thread-comment-box">
        <div>
          <div v-for="comment in thread.comments" :key="comment.pk" class="row thread-comment" >
            <div class="col-2">{{ comment.user.profile_info[0].nickname }}</div>
            <div v-if="currentUser.pk == comment.user.pk" class="col-8 d-flex justify-content-between">
              <div>{{ comment.content }}</div>
              <div style="padding:0">
              <button class="btn px-0" @click="trydelete(comment.pk)">삭제</button>
              </div>
            </div>
            <div v-else class="col-8">
              <div class="col-12">{{ comment.content }}</div>
            </div>
            <div class="col-2 created-string">{{ comment.created_string }}</div>
          </div>
        </div>
        <div>
          <comment-creation-form :threadPk="threadPk"></comment-creation-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import CommentCreationForm from '@/components/community/CommentCreationForm'
export default {
  name:"CommunityDetail",
  data() {
    return {
      threadPk: this.$route.params.threadPk,
    }
  },
  components:{
    CommentCreationForm
  },
  computed:{
    ...mapGetters(['thread', 'currentUser']),
    thread_poster_path() {
      return this.thread.movie ? 'https://image.tmdb.org/t/p/original' + this.thread.movie.poster_path : ""
    },
    title() {
      return this.thread.movie ? this.thread.movie.title : ""
    }
  },
  methods:{
    ...mapActions(['fetchThread', 'deleteComment']),
    trydelete(commentPk) {
      if (confirm('정말 삭제하시겠습니까?')) {
        const payload = {
          threadPk: this.threadPk,
          commentPk: commentPk
        }
        this.deleteComment(payload)
      }

    }
  },
  created() {
    this.fetchThread(this.threadPk)
  }
}
</script>

<style scoped>
  #thread-detail {
    color:white;
    padding: 30px;
  }
  h2 {
    margin-bottom: 20px;
  }

  #thread-poster{
    width:500px;
    border-radius: 10px;
  }
  #thread-comment-box {
    background: #36393f;
    color: black;
    padding:30px;
    width:700px;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .thread-comment{
    background: #ffffff;
    border-radius: 7px;
    height:37px;
    margin-bottom:10px;
    padding-top: 5px;
  }
  .col-8{
    padding-right:0;
  }
  .created-string{
    text-align: end;
  }
</style>