<template>
  <div class="d-flex justify-content-center align-items-center" style="height:1000px;">
    <div id="signup-box" class="d-flex flex-column justify-content-center align-items-center">
      <h3 id="signup-title">회원가입</h3> 
      <form @submit.prevent="signup(credentials)">
        <div id="signup-div">
          
          <div class="signup-comp">
            <p class="signup-label"><label for="username">아이디</label> <span v-if="usernameError" class="same-password">{{ usernameError }}</span></p>
            <input v-model="credentials.username" class="input-box" type="text" id="username" required autocomplete="off"/>
          </div>
          <div class="signup-comp">
            <p class="signup-label"><label for="password1">비밀번호</label></p>
            <input v-model="credentials.password1" class="input-box" type="password" id="password1" required placeholder="숫자, 영어, 특수문자 포함 8자리 이상으로 만들어주세요" />
          </div>
          <div class="signup-comp">
            <p class="signup-label"><label for="password2">비밀번호 확인</label>
            <span v-show="!passwordIdentify" class="same-password">위와 동일하게 입력해주세요</span>
            <span v-show="passwordIdentify" class="same-same">비밀번호가 일치합니다!</span>
            </p>
            <input v-model="credentials.password2" class="input-box" type="password" id="password2" required/>
          </div>
        </div>
        <button id="signup-btn">회원가입</button>
      </form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  // import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      // AccountErrorList,
    },
    data() {
      return {
        credentials: {
          password1: '',
          password2: '',          
        }
      }
    },
    computed: {
      ...mapGetters(['authError']),
      passwordIdentify() {
        if (this.credentials.password1.length === 0) {
          return false
        } else if (this.credentials.password1 === this.credentials.password2) {
          return true
        } else {
          return false
        }
      },
      // usernameError() {
      //   return this.authError ? this.authError.username[0] : false
      // }
    },
    methods: {
      ...mapActions(['signup']),
    },
  }
</script>


<style scoped>

#signup-box{  
  width: 566px;
  height: 748px;
  background-color: #36393f;
  filter: drop-shadow(0 0 4px #36393f);
  border-radius: 10px;
}

/* Rectangle 55 */
.input-box{
  width: 472px;
  height: 60px;
  background: #40444b;
  border: 1px solid rgba(255, 255, 255, 0.7);
  border-radius: 7px;
  margin-bottom: 20px;
}
input {
  padding: 0 0.5rem 0 0.5rem;
  color: #ffffff;
}
input::placeholder {
  color: #ffffff;
  opacity: 0.5;
}
#signup-btn{
  /* Rectangle 56 */
  width: 474px;
  height: 60px;
  margin-top:60px;
  margin-bottom:0px;

  /* logo */
  border: none;
  background: #E11616;
  border-radius: 7px;
  color: #ffffff;
}

.signup-comp {
  display: inline;
}
.Oauth-btn{
  width: 294px;
  height: 51px;
  border: #7A7373;
  border-radius: 7px;
}

.signup-label {
  color: #ffffff;
  margin-left:0rem;
  text-align: start !important;
  margin-bottom: 3px;
  margin-left: 1px;
}
.same-password {
  color: gold;
  margin-left: 0.5rem;
}
.same-same {
  color: gold;
  opacity: 0.4;
  margin-left: 0.5rem;
}
#signup-title{
  color:white;
  text-align: start;
  font-weight: 600;
  margin-bottom:30px;
}
</style>




