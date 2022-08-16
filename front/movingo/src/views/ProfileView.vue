<template>
  <div id="profile-view">
    <mypage-header v-if="isprofile" :profile_info="profileinfo" :username="profile.username"></mypage-header>
    <user-info :profile="profile" class="my-3" :isMe="isMe"></user-info>
    <mypage-nav :profile="profile"></mypage-nav>
  </div>
</template>

<script>
import MypageHeader from '@/components/mypage/MypageHeader'
import UserInfo from '@/components/mypage/UserInfo'
import MypageNav from '@/components/mypage/MypageNav'

import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  components:{
    MypageHeader,
    UserInfo,
    MypageNav,
  },
  computed: {
    ...mapGetters(['profile', 'isMe']),
    isprofile() {
      return this.profile ? true: false
    },
    profileinfo(){
      return this.profile.profile_info[0]
    }
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchCurrentBingo'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
    this.fetchCurrentBingo()
  },
}
</script>
<style scoped>
  #profile-view {
    background-color: #000000;
  }
</style>  
