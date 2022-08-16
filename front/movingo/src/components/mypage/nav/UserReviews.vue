<template>
  <div>
    <div v-if="reviewed !== 0" id="user-review-list" class="row">
      <div v-for="review in reviews" :key="review.pk" class="col-6">
        <user-review-item :review="review"></user-review-item>
      </div>
    </div>
    <div v-else>
      <h3>아직 작성한 리뷰가 없어요!</h3>
    </div>
  </div>
</template>

<script>
import UserReviewItem from './UserReviewItem'

export default {
  name: 'UserReviews',
  components: {
    UserReviewItem,
  },
  props: {
    reviews: Array,
  },
  computed: {
    reviewed() {
      return this.reviews.length
    }
  }
}
</script>

<style scoped>
h3{
  margin-top: 20px;
  margin-bottom: 15px;
  font-weight: bold;
}
</style>