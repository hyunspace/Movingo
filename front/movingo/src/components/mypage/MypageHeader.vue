<template>
  <div id="userinfo">
    <div id="background" class="d-flex align-items-center">
      <img id="background-img" style="top:-100px; width:100%;" src="https://image.tmdb.org/t/p/original/nQlJsL0NbBM2fyzhmFGVx63FKtW.jpg" alt="">
    </div>
    <div id="user-profile-image" v-if="current_username == username">
      <button id="edit-profile-btn" type="button" style="padding:0px; padding:0; border:none;" data-bs-toggle="modal" data-bs-target="#edit-profile">
        <img v-if="profile_info.profile_img == 1" style="height:100%; width:100%;" src="@/assets/KDW.png" alt="">
        <img v-if="profile_info.profile_img == 2" style="height:100%; width:100%;" src="@/assets/OHM.png" alt="">
        <img v-if="profile_info.profile_img == 3" style="height:100%; width:100%;" src="@/assets/KJH.png" alt="">
        <img v-if="profile_info.profile_img == 4" style="height:100%; width:100%;" src="@/assets/KHG.png" alt="">
        <img v-if="profile_info.profile_img == 5" style="height:100%; width:100%;" src="@/assets/KNR.png" alt="">
        <img v-if="profile_info.profile_img == 6" style="height:100%; width:100%;" src="@/assets/KHR.png" alt="">
      </button>
    </div>
    <div  id="user-profile-image"  v-else>
      <img v-if="profile_info.profile_img == 1" style="height:100%; width:100%;" src="@/assets/KDW.png" alt="">
      <img v-if="profile_info.profile_img == 2" style="height:100%; width:100%;" src="@/assets/OHM.png" alt="">
      <img v-if="profile_info.profile_img == 3" style="height:100%; width:100%;" src="@/assets/KJH.png" alt="">
      <img v-if="profile_info.profile_img == 4" style="height:100%; width:100%;" src="@/assets/KHG.png" alt="">
      <img v-if="profile_info.profile_img == 5" style="height:100%; width:100%;" src="@/assets/KNR.png" alt="">
      <img v-if="profile_info.profile_img == 6" style="height:100%; width:100%;" src="@/assets/KHR.png" alt="">
    </div>
    <div style="height:85px;"></div>
    <h2>{{ profile_info.nickname }}</h2>   
    <edit-profile :profile_info="profile_info" :username="username"></edit-profile>
  </div>

</template>

<script>
import { mapGetters } from 'vuex'
import EditProfile from './EditProfile'
export default {
  name: 'MypageHeader',
  props:{
    username:String,
    profile_info:Object,
  },
  components:{
    EditProfile
  },
  computed:{
    ...mapGetters(['currentUser']),
    nickname() {
      return this.profile ? this.profile.profile_info : ''
    },
    current_username() {
      return this.currentUser ? this.currentUser.username : ""
    }
    
  }
}
</script>

<style scoped>
#userinfo {
  position:relative;
}

#background {
  background-color: #36393f;
  width:100%;
  height: 400px;
  overflow: hidden;
}
#background-img{
  filter: contrast(80%) saturate(80%);
  filter: brightness(90%) blur(2px);
}

#user-profile-image {
  overflow: hidden;
  border: solid 3px black;
  position: absolute;
  background: #36393f;
  top: 325px;
  left: 44.212%;
  width:150px;
  height: 150px;
  border-radius: 100%;
}

h2 {
  text-align: center;
  font-weight: bold;
  color:white;
}

#edit-profile-btn:hover{
  opacity: 0.8;
}
</style>