<template>
  <div>
    <div id="review-list" v-if="reviewsExist">
      <movie-review-item
        v-for="review in reviews"
        :key="review.pk"
        :review="review"
        :movie="movie"
        ></movie-review-item>
    </div>
    <div v-else class="text-center">
      <p class="no-review">아직 작성된 리뷰가 없어요! <br>
      첫 번째 리뷰 작성자가 되어보세요!</p>
    </div>
  </div>
</template>

<script>
import MovieReviewItem from './MovieReviewItem'

export default {
  name: 'MovieReviewItems',
  props: {
    movie: Object,
    reviews: Array,
  },
  components: {
    MovieReviewItem,
  },
  computed: {
    reviewsExist() {
      return this.reviews ? this.reviews.length : 0
    }
  },
  methods: {
  },
  
}
</script>

<style scoped>
  #review-card {
    background-color: #ffffff;
    color: #000000;
    /* border: 2px solid red; */
    border-radius: 4px;
    margin: 0.7rem;
    padding: 0.7rem;
  }
  .no-review {
    display: block;
    margin-top: 5rem;
    padding-right: 0;
    padding-left: 20px;
  }
  .bi-star-fill {
    color: gold;
  }
  .user-profile {
    text-decoration: none;
    color: #000000;
  }
  .user-profile:hover {
    color: #36393f;
  }
  hr {
    color: #36393f;
    margin: 5px;
    padding: 0;
  }
</style>