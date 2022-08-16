<template>
  <div>

    <form @submit.prevent="onSubmit" class="row">
      <div class="d-flex justify-content-center mt-2">
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
      <input type="text" class="my-review-content" id="content" autocomplete="off" v-model="review.content" />
      <div class="d-flex justify-content-between px-0">
        <button @click="switchReview" class="justify-content-center go-back-btn review-ud-btn ">뒤로 가기</button>
        <div class="btns">
          <button class="review-ud-btn delete-btn" @click.prevent="deleteAndMove">삭제</button>
          <button class="review-ud-btn update-btn">수정</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewUpdateForm',
  props: {
    movie: Object,
  },
  computed: {
    ...mapGetters(['review'])
    },
  methods: {
    ...mapActions(['switchUserReview', 'updateReview', 'deleteReview']),
    switchReview() {
      this.switchUserReview({ moviePk: this.movie.pk, reviewPk: this.review.pk})
    },
    deleteAndMove() {
      this.deleteReview({ moviePk: this.movie.id, reviewPk: this.review.pk })
    }
  }
}
</script>

<style scoped>
  .my-review-content {
    border-radius: 6px;
    height: 10rem;
    margin: 10px 5px 10px 5px;
  }
  .go-back-btn {
    width: 15%;
    height: 2.5rem;
    background-color: #36393f;
    border-radius: 6px;
    color: #ffffff;
    margin-left: 8px;
  }
  .btns {
    width: 25%;
  }
  .delete-btn {
    background-color: #36393f;
    border-radius: 6px;
    color: #ffffff;
    width: 45%;
    height: 2.5rem;
    margin-right: 0.5rem;
  }
  .update-btn {
    background-color: #e1161e;
    border-radius: 6px;
    color: #ffffff;
    width: 45%;
    height: 2.5rem;
  }
  .review-ud-btn:hover {
    opacity: 0.8;
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