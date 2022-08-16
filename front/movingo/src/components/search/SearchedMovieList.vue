<template>
  <div class="row">
     <carousel id="mlc" :perPage=6 :scrollPerPage="false" :navigationEnabled="true" :paginationEnabled="false">
      <slide id="movie-list-slide" class="label mx-0" v-for="movie in movies" :key="movie.id">   
        <searched-movie-item data-bs-toggle="modal" data-bs-target="#movieDetail" :movie="movie"></searched-movie-item>  
      </slide>
    </carousel>
    <!-- <div v-for="movie in movies" :key="movie.pk" class="col-4">
      <searched-movie-item data-bs-toggle="modal" data-bs-target="#movieDetail" :movie="movie"></searched-movie-item>  
    </div> -->
    <movie-detail></movie-detail>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { Carousel, Slide } from 'vue-carousel'
import MovieDetail from '@/components/detail/MovieDetail'
import SearchedMovieItem from './SearchedMovieItem'
export default {
  name: "SearchedMovieList",
  components: {
    SearchedMovieItem, MovieDetail, Carousel, Slide,
  },
  computed: {
    ...mapGetters(['movies'])
  }
}
</script>

<style scoped>

</style>
