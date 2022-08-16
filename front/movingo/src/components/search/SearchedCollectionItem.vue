<template>
  <div id="searched-movie-poster">
    
  </div>
  
</template>

<script>
export default {
  name: "SearchedMovieItem",
  props: {
    movie:Object,
  },
  computed: {
    poster() {
      return this.movie.poster_path ? `https://image.tmdb.org/t/p/original/${ this.movie.poster_path }` : '..'
    },
  }
}
</script>

<style scoped>
#searched-movie-poster{
  width: 170px;
  height: 255px;
  margin-bottom:70px;
}
#searched-movie-poster > img {
  width:100%;
  height: 100%;
  
  border-radius: 10px;
}
</style>
