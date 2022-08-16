<template>
  <nav class="d-flex justify-content-between align-items-center text-light my-4">
    <div style="width:27rem;" class="nav-left">
      <ul class="d-flex justify-content-between align-items-center my-0 px-0" >
        <li class="m-0">
          <router-link :to="{ name: 'main' }" class="left-nav-item">
            <img src="../assets/logo.png" alt="로고" style="width:160px;">
          </router-link>          
        </li>
        <li id="home">
          <router-link :to="{ name: 'main' }" class="left-nav-item">홈</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'collections' }" class="left-nav-item">컬렉션</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'community' }" class="left-nav-item">커뮤니티</router-link>
        </li>
      </ul>
    </div>
    <div class="nav-right" style="width:18rem;">
      <ul class="d-flex justify-content-end align-items-center my-0">
        <li v-if="!isLoggedIn" class="mx-3">
          <router-link :to="{ name: 'login' }" class="right-nav-item">Login</router-link>
        </li>
        <li v-if="!isLoggedIn" class="mx-1">
          <router-link :to="{ name: 'signup' }" class="right-nav-item">Signup</router-link>
        </li>

        <li v-if="isLoggedIn" style="position:relative">
          <form @submit="searchThings(searchKeyword)">
            <div class="search-box">
              <div class="search-container">
                  <button class="search-icon"><i class="bi bi-search"></i></button>
                  <input autocomplete="off" @input="changeKeyword" :value="searchKeyword" type="search" id="search" placeholder="Search..." />
                  <auto-complete-suggestions id="suggestion-box" @titleFromSuggestions="fillSearchKeyword"></auto-complete-suggestions>
              </div>
            </div>
          </form>
        </li>
        <li id="for-loggedin" v-if="isLoggedIn" class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false" style="color:white">
            {{ nickname }} 님
          </a>  
          <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            <li>
              <router-link class="dropdown-item nav-item" :to="{ name: 'profile', params: { username } }">마이 페이지</router-link>
            </li>
            <li>
              <router-link class="dropdown-item nav-item" :to="{ name: 'logout' }">Logout</router-link>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AutoCompleteSuggestions from '@/components/AutoCompleteSuggestions'
  export default {
    name: 'NavBar',
    data() {
      return {
        searchKeyword: "",
      }
    },
    components: {
      AutoCompleteSuggestions
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
      nickname() {
        return this.currentUser.profile_info ? this.currentUser.profile_info[0].nickname : 'guest'
      },
    },
    methods: {
      ...mapActions(['fetchMovies', 'searchCollections', 'autoComplete']),
      searchThings(keyword) {        
        this.$router.push({ name: 'search_result', params: { keyword } })
      },
      fillSearchKeyword(keyword){
        this.searchKeyword = keyword
        
      },
      changeKeyword(event) {
        this.searchKeyword = event.target.value
        this.autoComplete(this.searchKeyword)
      }
    }
  }
</script>

<style scoped>
  a {
    color: white;
    text-decoration: none;
    font-size:20px;
    font-weight: 400;
  }
  ul {
    list-style:none;
  }
  .left-nav-item:hover {
    color: #40444b;
    font-weight: bolder;
  }
  .right-nav-item:hover {
    color: #40444b;
    font-weight: bolder;
  }
  .router-link-exact-active{
    font-weight: bold;
    text-decoration: none;
  }
  .dropdown-item {
    color:black;
  }

  /* search box */
  .search-box{
    width: 300px;
    height: 40px;
    font-size:20px;
  }
    .search-container{
    width: 300px;
    vertical-align: middle;
    white-space: nowrap;
    position: relative;
  }
  .search-container input#search{
    width: 50px;
    height: 40px;
    background: black;
    border: none;
    font-size: 15pt;
    float: right;
    color: #ff0000;
    padding-left: 20px;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    color: #ffffff;
    transition: width .55s ease;
  }
  .search-container input#search:-ms-input-placeholder {  
    color: #40444b;  
  }  
  .search-container input#search:focus, .search-container input#search:active{
    outline:none;
    width: 300px;
  }  
  .search-container:hover input#search{
    width: 300px;
    background: #40444b;
  }  
  .search-container:hover .icon{
    color: #ffffff;
    background: #40444b;
    opacity: 1;
  }
  #suggestion-box {
    position:absolute;
    /* visibility: hidden; */
    left:20px;
    z-index: 5;
  }
  .search-container .search-icon{
    padding-right:10px;
    background:black;
    position: absolute;
    border: none;
    top: -2px;
    left:82%;
    margin-left: 17px;
    margin-top: 6px;
    z-index: 1;
    color: #FFF;
  }
  .search-container input#search:focus, .search-container input#search:active{
    outline:none;
    width: 300px;
  }
  .search-container:hover input#search{
    width: 300px;
    background: #40444b;
  }
    .search-container:hover .search-icon{
    color: #ffffff;
    opacity: 0.8;
    background: #40444b;
  }
  #suggestion-box {
    position:absolute;
    font-size:15px;
    width: 300px;
    opacity: 0;
    top:50px;
    left:20px;
    z-index: 5;
  }
  input#search:focus{
    width: 300px;
    background: #40444b;
  }
  .search-container:focus-within #suggestion-box {
      opacity: 1;
  }
  .search-container:focus-within .search-icon{
    color: #ffffff;
    opacity: 0.8;
    background: #40444b;
  }
</style>
