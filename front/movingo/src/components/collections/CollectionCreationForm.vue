<template>
  <div class="modal fade" id="createcollection" tabindex="-1" aria-labelledby="createcollectionLabel" aria-hidden="true">
    <div class="modal-dialog modal-xl modal-dialog-centered">
      <div class="modal-content">
        <h4 class="add-new-movies">새 컬렉션</h4>
        <input autocomplete="off" v-model="newCollection.title" id="new-collection-title" type="text" placeholder="컬렉션 제목을 입력해주세요">
        <input autocomplete="off" v-model="newCollection.description" id="new-collection-description" type="text" placeholder="컬렉션 소개를 입력해주세요"> 
        <h5 class="add-new-movies">영화 담기</h5>
        <form class="d-flex" id="search-form" @submit.prevent="fetchMovies(search_keyword)">
          <input autocomplete="off" @input="changeKeyword" :value="search_keyword" type="search" id="nc-search-keyword" placeholder="영화제목을 입력해주세요" />
          <auto-complete-suggestions id="suggestion-box" @titleFromSuggestions="fillSearchKeyword"></auto-complete-suggestions>
          <button id="nc-search-button" class="btn">검색</button>
        </form>
        <div class="row px-0">
          <div class="col-6 px-0">
            <div id="searched-movie-box">
              <p v-if="!movies.length" class="notification">현재 검색된 영화가 없습니다.</p>
              <carousel id="searched-movie-list" :perPage=3 :navigationEnabled="true" :paginationEnabled="false">
                <slide id="searched-movie-list-slide" class="label mx-0" v-for="mv in movies" :key="mv.id">   
                  <img @click="selectMovie(mv)" type="button" class="movie-list-poster" style="width:153.42px; height:230px;" :src="`https://image.tmdb.org/t/p/original/${ mv.poster_path }`" alt="...">        
                </slide>
              </carousel>
            </div>
          </div>
          <div class="col-6 px-0">
            <div id="selected-movie-box">
              <p v-if="!newCollection.movies.length" class="notification">현재 담아둔 영화가 없습니다.</p>
              <carousel id="selected-movie-list" :perPage=3 :navigationEnabled="true" :paginationEnabled="false">
                <slide id="selected-movie-list-slide" class="label mx-0" v-for="smv in selected_movies_list" :key="smv.id">   
                  <img @click="deleteMovie(smv)" type="button" class="movie-list-poster" style="width:153.42px; height:230px;" :src="`https://image.tmdb.org/t/p/original/${ smv.poster_path }`" alt="...">        
                </slide>
              </carousel>
            </div>
          </div>
        </div>
        <div class="d-flex justify-content-end">
          <button class="btn mx-4 my-0" id="nc-close-btn" data-bs-dismiss="modal">취소</button>
          <button @click.prevent="onSubmit" class="btn mx-0 my-0" data-bs-dismiss="modal" id="nc-add-btn">확인</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel'
import AutoCompleteSuggestions from '@/components/AutoCompleteSuggestions'
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieDetail',
  props: {
    formCollection:Object,
    action: String, 
  },
    data(){
      return {
        search_keyword: "",
        newCollection:{
          title: this.formCollection.title,
          description: this.formCollection.description,
          movies: this.formCollection.movies,
        }
      }
    },
  computed: {
    ...mapGetters(['movie', 'movies']),
    selected_movies_list() {
      return this.newCollection.movies
    }
  },
  components:{
    Carousel, 
    Slide,
    AutoCompleteSuggestions,
  },
  methods:{
    ...mapActions(['fetchMovies', 'createCollection','updateCollection', 'autoComplete']),
    selectMovie(movie) {
      if (!this.newCollection.movies.includes(movie)) {
        this.newCollection.movies.push(movie)
      }
    },
    deleteMovie(movie) {
      const index = this.newCollection.movies.indexOf(movie)
      this.newCollection.movies.splice(index,1)
    },
    changeKeyword(event) {
      this.search_keyword = event.target.value
      this.autoComplete(this.search_keyword)
    },
    onSubmit() {
      if (this.action === 'create') {
        if (!this.newCollection.title || !this.newCollection.description) {
          alert('제목과 내용을 제대로 입력해주세요')
        } else {
          this.createCollection(this.newCollection)
        }
      } else if (this.action === 'update') {
        const payload = {
          pk: this.formCollection.pk,
          ...this.newCollection,
        }
        this.updateCollection(payload)
      }
    },
    fillSearchKeyword(keyword){
      this.search_keyword = keyword
      this.fetchMovies(this.search_keyword)
    },
  }
}
</script>

<style scoped>
#modal-header {
  text-align: right;
}
.modal-content {
  background: #000000;
  border:solid 2px #40444b;
  filter: drop-shadow(0 0 2px #40444b);
  border-radius: 10px;
  padding: 40px;
  padding-top: 50px;
  padding-bottom: 40px;
}
#new-collection-title {
  width: 703px;
  height: 62px;
  border:none;
  background: #40444b;
  padding: 10px;
  border-radius: 7px;
  margin: 10px 10px 0px 10px;
}
#new-collection-description { 
  height: 132px;
  border:none;
  background: #40444b;
  border-radius: 7px;
  padding: 10px;
  margin: 10px 10px 30px 10px;  
}
.add-new-movies{
  color:white;
  font-weight:500;
  margin-left:8px;
  margin-bottom:3px;
}
#nc-search-keyword{
  width:400px;
  height:42px;
  border:none;
  background: #40444b;
  border-radius: 7px;
  margin: 10px 10px 13px 10px;
  padding-left:10px
}
#nc-search-button{
  width: 60px;
  height: 41px;
  background: #ffffff;
  border-radius: 7px;
  margin-top: 10px;
  }
#nc-search-button:hover{
  opacity:0.8
}
#searched-movie-box{
  height: 250px;
  border-radius: 7px;
  background: #40444b;
  margin: 0px 15px 0px 22px;   
  padding: 10px;
}
input {
  color: #ffffff;
}
input::placeholder {
  color: #ffffff;
  opacity: 0.85;
}
.notification {
  color: #ffffff;
  opacity: 0.85;
  text-align: center;
  margin-top: 105px;
}
#selected-movie-box{
  height: 250px;
  border-radius: 7px;
  background: #40444b;
  margin: 0px 15px 25px 15px;
  padding: 10px;
}
#nc-close-btn{
  width: 70px;
  height: 38px;
  background: #ffffff;
  border-radius: 7px;
}
#nc-close-btn:hover{
  opacity: 0.8;
}
#nc-add-btn{
  width: 70px;
  height: 38px;
  background: #E11616;
  border-radius: 7px;
  color:white;
}
#nc-add-btn:hover{
  opacity: 0.8;
}
.VueCarousel{
  width:490px;
}
#searched-movie-list-slide{
  height:190;
  padding-left:5px;  
}
#selected-movie-list-slide{
  height:190;
  padding-left:5px;  
}
.movie-list-poster{
  border-radius:7px;
}
.movie-list-poster:hover{
  opacity: 0.5;
}
.add-new-movies{
  color:white;
  font-weight:500;
  margin-left:8px;
  margin-bottom:3px;
}
#suggestion-box {
  position:absolute;
  font-size:15px;
  width: 300px;
  opacity: 0;
  top:405px;
  color:white;
  left:55px;
  z-index: 5;
}

#search-form:focus-within #suggestion-box {
    opacity: 1;
}
</style>
