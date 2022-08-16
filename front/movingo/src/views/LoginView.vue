<template>
  <div class="d-flex justify-content-center align-items-center" style="height:1000px;">
    <div id="login-box" class="d-flex flex-column justify-content-center align-items-center">

      <h3 id="login-title">로그인</h3> 
      <account-error-list v-if="authError"></account-error-list>
      
      <form @submit.prevent="login(credentials)" class="text-center">
        <div id="login-div" >
          <div class="login-comp">
            <p class="login-label"><label for="username"> 아이디 </label></p>
            <input v-model="credentials.username" class="input-box px-2" type="text" id="username" required autocomplete="off"/>
          </div>
          <div class="login-comp my-3">
            <p class="login-label"><label for="password">비밀번호</label></p>
            <input v-model="credentials.password" class="input-box px-2" type="password" id="password" required />
          </div>
          <div class="login-comp">
            <button id="login-btn" class="my-3">로그인</button>
          </div>
        </div>
        
        <div class="d-flex justify-content-end">
          <a href=""><p>아이디 찾기</p></a>
          <p class="mx-2" style="color:white">|</p>
          <a href=""><p>비밀번호 재설정</p></a>
        </div>
        <p></p>
        <router-link class="Oauth-btn btn" style="background: #36393f; color:white; font-weight: 500; text-decoration:none; border: 1px solid #ffffff" :to="{ name: 'signup' }"><p class="my-2">회원가입</p></router-link>
      </form>
    
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style scoped>
ul {
 list-style: none; 
}
a {
  color: white;
  text-decoration: none;
}
#login-box{  
  width: 566px;
  height: 748px;
  background-color: #36393f;
  filter: drop-shadow(0 0 4px #36393f);
  border-radius: 10px;
}
#username{
  margin-bottom: 10px;
}
/* Rectangle 55 */
.input-box{
  width: 472px;
  height: 60px;
  background: #40444b;
  border: 1px solid rgba(255, 255, 255, 0.7);
  border-radius: 7px;
}
input {
  color: #ffffff;
}
#login-btn{
  /* Rectangle 56 */
  width: 474px;
  height: 60px;
  border:none;
  /* logo */
  background: #E11616;
  border-radius: 7px;
  color: #ffffff;
}
#login-title{
  color:white;
  text-align: start;
  font-weight: 600;
  margin-bottom:30px;
}

.login-comp {
  margin-top:5px;
  height: 90px;
}
.Oauth-btn{
  padding:4px;
  margin-top: 100px;
  width: 294px;
  height: 51px;
  border: #7A7373;
  border-radius: 7px;
}
.login-label {
  color:white;
  /* margin-left:3rem !important; */
  text-align: start !important;
  margin-bottom: 3px;
}

</style>







