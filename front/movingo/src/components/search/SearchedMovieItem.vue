<template>
  <div id="searched-movie-poster"  @click="[fetchMovie(movie.pk), fetchTrailerURI(movie.title)]">
    <img :src="poster" alt="" >
    <p class="text-center my-2">{{ movie.title }}</p>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: "SearchedMovieItem",
  props: {
    movie:Object,
  },
  computed: {
    poster() {
      return this.movie.poster_path ? `https://image.tmdb.org/t/p/original/${ this.movie.poster_path }` : '..'
    },
  },
  methods: {
    ...mapActions(['fetchMovie', 'fetchTrailerURI'])
  }
}
</script>

<style scoped>
#searched-movie-poster > p {
  position: inherit;
}
#searched-movie-poster{
  width: 178px;
  height: 268px;
  margin:0;
  margin-bottom:70px;
}
#searched-movie-poster:hover{
  filter:brightness(0.7);
  cursor: pointer;
}
#searched-movie-poster > img {
  width:100%;
  height: 100%;
  
  border-radius: 10px;
}
</style>
