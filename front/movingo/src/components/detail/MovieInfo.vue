<template>
  <div id="movie-info" class="my-2">
    <h2>{{ movie.title }}</h2>
    <div class="d-flex">
      <p class="mx-1">{{ movie.release_date }} 개봉 |</p>
      <div class="star-ratings mx-1">
        <span 
          class="star-ratings-fill space-x-2 text-lg"
          :style="{ width: ratingToPercent + '%' }"
        >
          <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
        </span>
        <div class="star-ratings-base space-x-2 text-lg">
          <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
        </div>
      </div>    
      <p class="mx-1">{{ movie.vote_average }} | </p>
      <span class="mx-1" v-for="genre in movie.genres" :key="genre.id">{{ genre.name }} </span>
    </div>
      
    <br>  
    <div>{{ overview }}...</div>
    <div id="movie-info-buttons" class="d-flex justify-content-start align-items-center">
      <div v-if="wished" class="movie-wish text-center mx-1">
        <button @click="wishMovie(movie.pk)" class="movie-detail-button"><i class="bi bi-heart-fill movie-like"></i></button>
        <p class="movie-wish-cnt mx-2">{{ wish_cnt }}</p>
      </div>
      <div v-if="!wished" class="movie-wish text-center mx-1">
        <button @click="wishMovie(movie.pk)" class="movie-detail-button"><i class="bi bi-heart movie-like"></i></button>
        <p class="movie-wish-cnt">{{ wish_cnt }}</p>
      </div>
      <div>
        <div v-if="hasThread" >
          <button data-bs-dismiss="modal" @click="gotoThreadDetail(movieThread.threadPk)" class="yes-community-btn">커뮤니티 바로가기</button>
        </div>
        <div v-if="!hasThread">
          <button data-bs-dismiss="modal" @click="createThread(movie.pk)" class="no-community-btn">새 커뮤니티 만들기</button>
          <span class="no-community">아직 커뮤니티가 없어요😂</span>
        </div>
      </div>
      <!-- <div>
         <button class="movie-detail-button"><i class="movie-add bi bi-plus-lg"></i></button>
         <p style="color: black;">.</p>
      </div> -->
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieInfo',
  props: {
    movie:Object,
  },
  computed: {
    ...mapGetters(['currentUser', 'movieThread']),
    overview() {
      return String(this.movie.overview).substr(0, 200)
    },
    wished() {
    return this.movie.wish_users ? this.movie.wish_users.filter(element => {
      return element.pk == this.currentUser.pk
      }).length : false
    },
    wish_cnt() {
      return this.movie.wish_count
    },
    ratingToPercent() {
      const score = this.movie.vote_average * 10
      return score + 3.5      
    },
    hasThread() {
      return this.movieThread.threadPk === -1 ? false : true
    }
  },
  methods: {
    ...mapActions(['wishMovie', 'moveToThread', 'createThread']),
    gotoThreadDetail(pk) {
      this.$router.push({name: 'community_detail', params: { threadPk: pk }})
    }
  }
}
</script>

<style scoped>
  #movie-info{ 
    color:white;
  }
  #movie-info-buttons{
    margin-top:8px;
  }
  .movie-wish {
    width: 25px;
  }
  .movie-like {
    color:#E11616;
    font-size: 25px;
  }
  .movie-detail-button {
    background: #000000;
    padding:0px;
  }
  .movie-wish-cnt {
    font-size:13px;
    margin-left:4px;
  }
  .movie-add{
    color:#FFFFFF;
    margin-left: 6px;
    font-weight: bold;
    font-size: 25px;
  }
  .bi-plus-lg {
    margin-bottom: 2px;
  }
  .rate-number {
    margin-left: 2px;
  }
  button:hover {
    opacity: 0.8;
  }
  .yes-community-btn {
    background-color: #36393f;
    border-radius: 6px;
    color: #ffffff;
    margin: 8px 8px 8px 15px;
    padding: 6px;
  }
  .yes-community-btn:hover{
    background-color: #e11616;
  }
  .no-community-btn {
    background-color: #36393f;
    border-radius: 6px;
    color: #ffffff;
    margin: 8px 8px 8px 15px;
    padding: 6px;
  }

  /* 별 채우기 */
  .star-ratings {
    color: #aaa9a9; 
    position: relative;
    unicode-bidi: bidi-override;
    width: max-content;
    -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
    -webkit-text-stroke-width: 0.5px;
    -webkit-text-stroke-color: rgb(255, 226, 62);
  }
  .star-ratings-fill {
    color: #fff58c;
    padding: 0;
    position: absolute;
    z-index: 1;
    display: flex;
    top: 0;
    left: 0;
    overflow: hidden;
    -webkit-text-fill-color: gold;
  } 
  .star-ratings-base {
    z-index: 0;
    padding: 0;
  }
</style>