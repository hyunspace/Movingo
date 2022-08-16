<template>
  <div class="d-flex justify-content-between" id="cp-item">
    <div id="community-card">
      <div>
        <img id="community-poster" style="width:100%" :src="poster_path" alt="">
      </div>
      <div id="community-title">
        <p>{{ thread.movie.title }}</p>
      </div>
    </div>
    <div class="community-comments d-flex flex-column justify-content-evenly">
      <div v-for="comment in comments" :key="comment.pk" class="row thread-comments d-flex align-items-center">
        <div class="col-2" style="padding-left:20px;">{{ comment.user.profile_info[0].nickname }}</div>
        <div class="col-8">{{ comment.content }}</div>
        <div class="col-2 text-end created-time">{{ comment.created_string }}</div>
      </div>
    </div>
    <div class="cm-btns d-flex flex-column justify-content-between">
      <button @click="gotoThreadDetail" style="background:transparent; border:none; color:white; margin-left:22px;">더보기 ></button>
      
    </div>
  </div>
</template>

<script>

import _ from 'lodash'
export default {
  name: "CommunityPoster",
  props:{
    thread:Object,
  },
  computed:{
    poster_path() {
      return  this.thread.movie ? 'https://image.tmdb.org/t/p/original' + this.thread.movie.poster_path : "../assets/logo.png"
    },
    comments() {
      let this_thread = this.thread.comments
      return _.sortBy(this_thread, 'created_at').reverse().splice(0,4)
    },
    updated_time() {
      let this_thread = this.thread.comments
      return this_thread ? _.sortBy(this_thread, 'created_at').reverse().splice(0,1)[0].created_string : ""
    },
    noComment() {
      return _.max([this.thread.comment_count - 4, 0])
    }
  },
  methods: {
    gotoThreadDetail() {
      this.$router.push({name: 'community_detail', params: { threadPk: this.thread.pk }})
    }
  }
}
</script>

<style scoped>
#cp-item{
  background: #36393f;
  margin: 20px;
  padding: 20px;
  border-radius: 7px;
}
#toThreadDetail{
  border: none;
  background: transparent;
  color:white;
}
#community-card{
  width:170px;
  border-radius: 7px;
  background:white;
  padding: 7px;
  height:257px;
  margin-bottom: 0px;
}
#community-poster{
  border-radius: 7px;
}
#community-title{
  color:black;
  display:flex;
  align-items: center;
  justify-content: center;
  margin-top: 2px;
}
#community-comments{
  height: 257px;
  padding: 7px 9px 7px 7px;
}
.thread-comments{
  background:white;
  color:black;
  height: 45px;
  border-radius: 7px;
  width:860px;
}
.cm-btns {
  padding-top:15px;
  padding-bottom:20px;
}
</style>