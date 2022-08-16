<template>
  <div id="review-creation-form">
    <div v-if="!firstReview.isFirstReview">
      <form @submit.prevent="onSubmit" class="row">
        <div class="d-flex justify-content-center">
          <fieldset class="rate">
            <input type="radio" id="rating10" name="rating" value="10" v-model="review.rate" /><label for="rating10" title="5 stars"></label>
            <input type="radio" id="rating9" name="rating" value="9" v-model="review.rate" /><label class="half" for="rating9" title="4 1/2 stars"></label>
            <input type="radio" id="rating8" name="rating" value="8" v-model="review.rate" /><label for="rating8" title="4 stars"></label>
            <input type="radio" id="rating7" name="rating" value="7" v-model="review.rate" /><label class="half" for="rating7" title="3 1/2 stars"></label>
            <input type="radio" id="rating6" name="rating" value="6" v-model="review.rate" /><label for="rating6" title="3 stars"></label>
            <input type="radio" id="rating5" name="rating" value="5" v-model="review.rate" /><label class="half" for="rating5" title="2 1/2 stars"></label>
            <input type="radio" id="rating4" name="rating" value="4" v-model="review.rate" /><label for="rating4" title="2 stars"></label>
            <input type="radio" id="rating3" name="rating" value="3" v-model="review.rate" /><label class="half" for="rating3" title="1 1/2 stars"></label>
            <input type="radio" id="rating2" name="rating" value="2" v-model="review.rate" /><label for="rating2" title="1 star"></label>
            <input type="radio" id="rating1" name="rating" value="1" v-model="review.rate" /><label class="half" for="rating1" title="1/2 star"></label>
          </fieldset>
        </div>
        <div class="d-flex">
          <input type="text" class="form-control" v-model="review.content" id="content" autocomplete="off" placeholder="리뷰 내용을 작성해주세요"/>
          <button class="enroll-btn">등록</button>
        </div>
      </form>
    </div>
    <div v-else>
      <div class="text-center">
      <p>이전에 작성한 리뷰가 있어요!</p>
      <p>이전 리뷰를 수정하거나 삭제 후 새로 작성해주세요</p>
      <button @click="switchReview" class="my-review-btn justify-content-center"
        >내 리뷰 보기</button>
    </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
// import ReviewUpdateForm from './ReviewUpdateForm.vue'

export default {
  name: "ReviewCreationForm",
  components: {
    // ReviewUpdateForm
  },
  data(){
    return {
      review:{
        rate: '',
        content: '',
      },
    }
  },
  props:{
    movie: Object,
    firstReview: Object,
  },
  computed: {
    ...mapGetters(['currentUser']),
    isFirstReview() {
      return this.movie.reviews.filter(element => {
        return element.user.pk == parseInt(this.currentUser.pk)
      }).length
    },
    findReviewPk() {
      const theReview = this.movie.reviews.filter(element => {
          return element.user.pk == parseInt(this.currentUser.pk)
        })    
        return theReview[0].pk
    }
  },
  methods: {
    ...mapActions(['createReview', 'switchUserReview', 'fetchReview']),
    onSubmit() {
      this.createReview({ moviePk: this.movie.pk, rate: this.review.rate, content: this.review.content })
      this.review.rate = ''
      this.review.content = ''
    },
    switchReview() {
      console.log('switchReview 실행함')
      // console.log(this.movie.pk) // 102382
      // console.log(this.findReviewPk) // 4
      this.fetchReview({ moviePk: this.movie.pk, reviewPk: this.findReviewPk})
      this.switchUserReview({ moviePk: this.movie.pk, reviewPk: this.findReviewPk})
    }
  },
}
</script>

<style scoped>
#review-creation-form {
  padding: 0.7rem;
}
option {
  color:#000000;
}
.form-control {
  height: 2.5rem;
}
button:hover {
  opacity: 0.8;
}
.enroll-btn {
  border-radius: 6px;
  background-color: #e1161e;
  color: #ffffff;
  margin-left: 0.7rem;
  width: 15%;
  height: 2.5rem;
}
.my-review-btn {
  background-color: #36393f;
  border-radius: 6px;
  color: #ffffff;
  margin-top: 0.4rem;
  width: 30%;
  height: 2.2rem;
}

/* 별점 */
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);
/* Ratings widget */
.rate {
    display: inline-block;
    border: 0;
}
/* Hide radio */
.rate > input {
    display: none;
}
/* Order correctly by floating highest to the right */
.rate > label {
    float: right;
}
/* The star of the show */
.rate > label:before {
    display: inline-block;
    font-size: 1.5rem;
    padding: .3rem .2rem;
    margin: 0;
    cursor: pointer;
    font-family: FontAwesome;
    content: "\f005 "; /* full star */
}

/* Half star trick */
.rate .half:before {
    content: "\f089 "; /* half star no outline */
    position: absolute;
    padding-right: 0;
}
/* Click + hover color */
input:checked ~ label, /* color current and previous stars on checked */
label:hover, label:hover ~ label { color: gold;  } /* color previous stars on hover */

/* Hover highlights */
input:checked + label:hover, input:checked ~ label:hover, /* highlight current and previous stars */
input:checked ~ label:hover ~ label, /* highlight previous selected stars for new rating */
label:hover ~ input:checked ~ label /* highlight previous selected stars */ { color: gold;  } 
</style>