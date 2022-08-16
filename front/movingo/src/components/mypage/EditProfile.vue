<template>
  <div class="modal fade" id="edit-profile" tabindex="-1" aria-labelledby="edit-profile" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <form @submit="editProfile">
          <div class="text-center" style="margin:20px;"><h3>프로필 사진</h3></div>
          <div class="d-flex flex-column justify-content-center">
            <div class="d-flex justify-content-center">
              <div>
                <input type="radio" id="pfi_1" name="profile-img-x" value="1" v-model="edited_profile.profile_img">
                <label for="pfi_1"><img class="profile-img-ex" src="@/assets/KDW.png" alt=""></label> 
              </div>
              <div>
                <input type="radio" id="pfi_2" name="profile-img-x" value="2" v-model="edited_profile.profile_img">
                <label for="pfi_2"><img class="profile-img-ex" src="@/assets/OHM.png" alt=""></label>
              </div>
              <div>
                <input type="radio" id="pfi_3" name="profile-img-x" value="3" v-model="edited_profile.profile_img">
                <label for="pfi_3"><img class="profile-img-ex" src="@/assets/KJH.png" alt=""></label>
              </div>
            </div>
            <div class="d-flex justify-content-center">
              <div>
                <input type="radio" id="pfi_4" name="profile-img-x" value="4" v-model="edited_profile.profile_img">
                <label for="pfi_4"><img class="profile-img-ex" src="@/assets/KHG.png" alt=""></label>
              </div>
              <div>
                <input type="radio" id="pfi_5" name="profile-img-x" value="5" v-model="edited_profile.profile_img">
                <label for="pfi_5"><img class="profile-img-ex" src="@/assets/KNR.png" alt=""></label>
              </div>
              <div>
                <input type="radio" id="pfi_6" name="profile-img-x" value="6" v-model="edited_profile.profile_img">
                <label for="pfi_6"><img class="profile-img-ex" src="@/assets/KHR.png" alt=""></label>
              </div>
            </div>
          </div>
          <div style="margin:40px;">
            <div class="text-center"><h3>닉네임</h3></div>
            <div class="text-center">
              <input id="next-nickname" v-model="edited_profile.nickname" type="text">
            </div>
          </div>
          <div class="d-flex justify-content-center">
            <button class="cancel-profile-btn mx-2" data-bs-dismiss="modal">취소</button>
            <button class="edit-profile-btn mx-2">변경</button>
          </div>
        </form>
      </div>
    </div>
  </div>

</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: "EditProfile",
  props: {
    username: String, 
    profile_info:Object,
  },
  data() {
    return {
      edited_profile: {
        profile_img: this.profile_info.profile_img,
        nickname: this.profile_info.nickname,
      }
    }
  },
  methods:{
    ...mapActions(['updateProfile']),
    editProfile() {
      console.log(this.edited_profile)
      let payload = {
        username: this.username,
        profile_info: this.edited_profile,
      }
      this.updateProfile(payload)
    }
  }

}
</script>

<style scoped>
.modal-content{
  height:500px;
  background: #40444b;
  color: #ffffff;
}
.profile-img-ex{
  width: 100px;
  height: 100px;
  border: solid 2px #36393f;
  border-radius: 7px;
  box-shadow: 1mm;
  margin-left: 10px;
  margin-right: 20px;
}
.cancel-profile-btn {
  border-radius: 7px;
  padding:10px;
  padding-top:5px;
  padding-bottom:5px;
  border: transparent;
}
.edit-profile-btn {
  border-radius: 7px;
  padding:10px;
  padding-top:5px;
  padding-bottom:5px;
  background: #e11616;
  color: #ffffff;
  border: transparent;
}
#next-nickname{
  margin:0;
  margin-top:5px;
  border-radius: 7px;
  width: 200px;
  height:35px;
}

div > input {

  margin-left: 20px;
}
</style>