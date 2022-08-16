<template>
  <div>
    <carousel v-if="isLoggedIn" :perPage=1 :autoplay="true" :paginationEnabled="false">
      <slide>
        <img src="https://image.tmdb.org/t/p/original/AbgEQO2mneCSOc8CSnOMa8pBS8I.jpg" class="d-block w-100" alt="메인 배너 이미지">
      </slide>
      <slide>
        <img src="https://image.tmdb.org/t/p/original/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg" class="d-block w-100" alt="메인 배너 이미지">
      </slide>
      <slide>
        <img src="https://image.tmdb.org/t/p/original/zqkmTXzjkAgXmEWLRsY4UpTWCeo.jpg" class="d-block w-100" alt="메인 배너 이미지">
      </slide>
      <slide>
        <img src="https://image.tmdb.org/t/p/original/jL6B8mm9TR8vmh9VtgEg0GC7jPy.jpg" class="d-block w-100" alt="메인 배너 이미지">
      </slide>
    </carousel>
    <carousel v-else>
      <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdE1wr9%2FbtrCITXNYYJ%2FLRoBCdWOezZAq9ViBMjJ7k%2Fimg.png" class="d-block w-100" alt="로그인 또는 회원가입 하세요">
    </carousel>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel'
import { mapGetters } from 'vuex'

export default {
  name: 'MainCarousel',
  components:{
    Carousel, Slide
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  methods: {
  },
}
</script>

<style scoped>
</style>
