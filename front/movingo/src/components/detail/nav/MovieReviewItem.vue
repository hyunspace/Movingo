<template>
  <div>
    <div id="review-cards">
      <div id="review-card">
        <div id="review-card-body">
          <div class="review-card-user d-flex justify-content-between mx-2">
            <p @click="movetoProfile(review.user.username)"
              class="user-profile" data-bs-dismiss="modal">
              {{ review.user.profile_info[0].nickname }} 
            </p>
            <p><i class="bi bi-star-fill"></i> {{ review.rate }}</p>
          </div>
          <hr>
          <div class="review-card-content mx-2">
            {{ review.content }}
          </div>
          <hr>
          <div class="btns d-flex justify-content-between">
            <div class="like-btns mx-2">
              <div v-if="like" class="mx-1 d-flex">
                <button @click="likeReview({ moviePk: movie.pk, reviewPk: review.pk })" class="like-btn"><i class="bi bi-heart-fill"></i></button>
                <p class="mx-2">{{ review.like_users_cnt }}</p>
              </div>
              <div v-if="!like" class="mx-1 d-flex">
                <button @click="likeReview({ moviePk: movie.pk, reviewPk: review.pk })" class="like-btn"><i class="bi bi-heart"></i></button>
                <p class="mx-2">{{ review.like_users_cnt }}</p>
              </div>  
            </div>
            <div class="user-btn" v-if="sameUser">
              <button class="delete-btn" @click.prevent="deleteReview({ moviePk: movie.pk, reviewPk: review.pk })">삭제</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieReviewItem',
  props: {
    movie: Object,
    review: Object,
  },
  data() {
    return {
      payload: {
        moviePk: this.movie.pk,
        reviewPk: this.review.pk,
        rate: this.review.rate,
        content: this.review.content,
      }
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    like() {
      if (this.review.like_users.includes(this.currentUser.pk)) {
        return true
      } else {
      return false}
    },
    sameUser() {
      if (this.currentUser.pk === this.review.user.pk) {
        return true
      } else {
        return false
      }
    }
  },
  methods: {
    ...mapActions(['likeReview', 'deleteReview', 'updateReview']),
    onUpdate() {
      this.updateReview(this.payload)
    },
    movetoProfile(username){
      this.$router.push({ name: 'profile', params: {username: username} })
    }
  },
  
}
</script>

<style scoped>
  .user-profile:hover{
    cursor: pointer;
    opacity: 0.8;
  }
  #review-card {
    background-color: #ffffff;
    color: #000000;
    /* border: 2px solid red; */
    border-radius: 4px;
    width: 97.5%;
    margin: 0.7rem;
    padding: 0.7rem;
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
  .btns, .like-btn, .user-btn {
    background-color: #ffffff;
    border: transparent;

  }
  .like-btn {
    margin: 0px;
    padding-left: 0px;
  }
  .update-btn {
    background-color: #36393f;
    color: #ffffff;
    border: transparent;
    border-radius: 4px;
    margin-right: 0.5rem;
    padding: 0.1rem 0.3rem;
  }
  .delete-btn {
    background-color: #E11616;
    color: #ffffff;
    border: transparent;
    border-radius: 4px;
    padding: 0.1rem 0.3rem;
  }
  .bi-heart-fill {
    background-color: #ffffff;
    color: #E11616;
  }
  .bi-heart {
    background-color: #ffffff;
    color: #E11616;
  }
  hr {
    color: #36393f;
    margin: 5px;
    padding: 0;
  }
</style>