<template>
  <div>
    <div v-if="!onlyUserReview">
      <div id="reviews">
        <movie-review-items
          :movie="movie"
          :reviews="movie.reviews"
          >
        </movie-review-items>
      </div>
      <review-creation-form :movie="movie" :firstReview="{ isFirstReview }"></review-creation-form>
    </div>
    <div v-else>
      <review-update-form :movie="movie"></review-update-form>
    </div>
  </div>
</template>

<script>
import MovieReviewItems from './MovieReviewItems'
import ReviewCreationForm from './ReviewCreationForm'
import ReviewUpdateForm from './ReviewUpdateForm.vue'
import { mapGetters } from 'vuex'

export default {
  name: "MovieReviews",
  components:{
    MovieReviewItems,
    ReviewCreationForm,
    ReviewUpdateForm,
  },
  props:{
    movie: Object,
  },
  computed: {
    ...mapGetters(['onlyUserReview', 'currentUser']),
    isFirstReview() {
      return this.movie.reviews ? this.movie.reviews.filter(element => {
        return element.user.pk === this.currentUser.pk
      }).length : 0
    },
  },
  methods: {
  },
  
}

</script>

<style scoped>
  #reviews {
    width: 100%;
    height: 11rem;
    overflow-y: scroll;
    padding-right: 0;
  }
  #reviews::-webkit-scrollbar {
    /* display: none; */
    background-color: #000000;
  }
  #reviews::-webkit-scrollbar-thumb {
    /* display: none; */
    background-color: #343a40;
  }
  
</style>