<template>
  <div>
    <user-info :profile="profile" :username="profile.username" class="my-3"></user-info>
    <mypage-header v-if="profile" :profile="profile"></mypage-header>
  </div>
</template>

<script>
import MypageHeader from '@/components/mypage/upside/MypageHeader'
import UserInfo from '@/components/mypage/upside/UserInfo'


export default {
  name: 'ProfileView',
  props: {
    username:String,
    profile:Object,
  },
  components:{
    MypageHeader,
    UserInfo
  },
  computed: {
  },
  methods: {
  },
  created() {
  },
}
</script>

<style scoped>

</style>
