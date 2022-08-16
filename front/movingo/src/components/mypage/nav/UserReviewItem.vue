<template>
  <div style="padding:20px;">
    <div id="reviewitem" class="row">
      <div class="col-4" style="padding-left: 15px;">
        <img :src="poster" alt="" style="width:150px; height:220px; border-radius:7px;">
      </div>
      <div class="col-8 review-card">
        <div class="review-header d-flex justify-content-between">
          <h5 class="review-title">{{ title }}</h5>
          <p class="review-rate"><i class="bi bi-star-fill"></i> {{ review.rate }}</p> 
        </div>
        <div class="review-genres d-flex">
          <div v-for="genre in review.movie.genres" :key="genre.id" >
            <span v-if="genre.name=='모험'" class="adventure">{{ genre.name }}</span>
            <span v-if="genre.name=='판타지'" class="fantasy">{{ genre.name }}</span>
            <span v-if="genre.name=='애니메이션'" class="animation">{{ genre.name }}</span>
            <span v-if="genre.name=='드라마'" class="drama">{{ genre.name }}</span>
            <span v-if="genre.name=='공포'" class="horror">{{ genre.name }}</span>
            <span v-if="genre.name=='액션'" class="action">{{ genre.name }}</span>
            <span v-if="genre.name=='코미디'" class="comedy">{{ genre.name }}</span>
            <span v-if="genre.name=='역사'" class="history">{{ genre.name }}</span>
            <span v-if="genre.name=='서부'" class="western">{{ genre.name }}</span>
            <span v-if="genre.name=='스릴러'" class="thriller">{{ genre.name }}</span>
            <span v-if="genre.name=='범죄'" class="crime">{{ genre.name }}</span>
            <span v-if="genre.name=='다큐멘터리'" class="documentary">{{ genre.name }}</span>
            <span v-if="genre.name=='SF'" class="sf">{{ genre.name }}</span>
            <span v-if="genre.name=='미스터리'" class="mystery">{{ genre.name }}</span>
            <span v-if="genre.name=='음악'" class="music">{{ genre.name }}</span>
            <span v-if="genre.name=='로맨스'" class="romance">{{ genre.name }}</span>
            <span v-if="genre.name=='가족'" class="family">{{ genre.name }}</span>
            <span v-if="genre.name=='전쟁'" class="war">{{ genre.name }}</span>
            <span v-if="genre.name=='TV 영화'" class="tvshow">{{ genre.name }}</span>

          </div>
        </div>
        <hr>
        <div class="review-content">
          <p>{{ review.content }}</p>
        </div>
        <hr>
        <div class="extra d-flex justify-content-between">
          <p class="like-text">좋아요 {{ review.like_users_cnt }}개</p>
          <!-- <div class="btns">
            <button class="update-btn">수정</button>
            <button class="delete-btn" @click="deleteReview">삭제</button>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'UserReviewItem',
  props: {
    review: Object
  },
  data() {
    return {
      genrename: '',
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    poster() {
      return `https://image.tmdb.org/t/p/original/${ this.review.movie.poster_path }`
    },
    title() {
      let title = String(this.review.movie.title)
      return title.length > 17 ? title.substr(0, 17) + '..' : title 
    },
    genreStyle() {
      let checkGenre = this.genre.name
      console.log(checkGenre)
      switch (checkGenre) {
        case '모험':
          return 'adventure'
        case '판타지':
          return 'fantasy'
        case '애니메이션':
          return 'animation'
        default:
          return 'default-genre'
      }
    }
  },
  methods: {
    ...mapActions(['deleteUserReview']),
    deleteReview() {
      const reviewpk = this.review.pk
      this.deleteUserReview(reviewpk)
    },    
  }
}
</script>

<style scoped>
  #reviewitem{
    background: #ffffff;
    padding: 15px 10px 15px 0px;
    border-radius:7px;
    color: #36393f
  }
  .review-genres {
    margin-bottom: 10px;
  }
  .rm-genres{
    border-radius: 7px;
    background: black;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .review-card {
    padding-left: 0px;
  }
  .review-title{
    width: 85%;
    margin: 5px 0px 10px 0px;
    font-weight: bold;
  }
  .review-rate {
    margin-top: 10px;
    font-weight: bold;
  }
  hr {
    margin: 5px 0px 2px 0px;
  }
  .review-content {
    margin-top: 5px;
    height: 100px;
  }
  .bi-star-fill{
    color:gold;
  }
  .like-text {
    margin-top: 7px;
  }
  .btns {
    margin-top: 4px;
  }
  .update-btn {
    background-color: #36393f;
    border: transparent;
    border-radius: 6px;
    color: #ffffff;
    height: 2rem;
    margin-right: 0.5rem;
  }
  .delete-btn {
    background-color: #e1161e;
    border: transparent;
    border-radius: 6px;
    color: #ffffff;
    height: 2rem;
  }
  /* genre color */
  .adventure {
    border-radius: 7px;
    background: #e76f51;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .fantasy {
    border-radius: 7px;
    background: #5e548e;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .animation {
    border-radius: 7px;
    background: #fcbf49;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .drama {
    border-radius: 7px;
    background: #ffb5a7;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .horror {
    border-radius: 7px;
    background: #6a040f;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .action {
    border-radius: 7px;
    background: #c1121f;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .comedy {
    border-radius: 7px;
    background: #8ac926;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .history {
    border-radius: 7px;
    background: #52796f;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .western {
    border-radius: 7px;
    background: #432818;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .thriller {
    border-radius: 7px;
    background: #bc4749;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .crime {
    border-radius: 7px;
    background: #001233;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .documentary {
    border-radius: 7px;
    background: #619b8a;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .sf {
    border-radius: 7px;
    background: #480ca8;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .mistery {
    border-radius: 7px;
    background: #33415c;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .music {
    border-radius: 7px;
    background: #5fa8d3;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .romance {
    border-radius: 7px;
    background: #ffb3c6;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .family {
    border-radius: 7px;
    background: #ffd166;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .war {
    border-radius: 7px;
    background: #370617;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .tvshow {
    border-radius: 7px;
    background: #00bbf9;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
</style>