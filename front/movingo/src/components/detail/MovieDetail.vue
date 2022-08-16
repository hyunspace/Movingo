<template>
  <div class="modal fade" id="movieDetail" tabindex="-1" aria-labelledby="movieDetail" aria-hidden="true">
    <div class="modal-dialog modal-xl modal-dialog-centered">
      <div class="modal-content">
        <div id="modal-header">
          <button type="button" class="close-btn m-1" data-bs-dismiss="modal" aria-label="Close">
            <i class="bi bi-x-lg mx-1"></i>
          </button>
        </div>
        <div id="modal-body" v-if="movie" class="row">          
          <div id="poster-box" class="mx-4 col-5">
            <img id="poster" :src="poster" alt="">
          </div>
          <div class="col-6">
            <movie-info id="movie-info" :movie="movie"></movie-info>
            <movie-nav id="movie-nav" :movie="movie"></movie-nav>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import MovieInfo from './MovieInfo.vue'
import MovieNav from './MovieNav.vue'
export default {
  name: 'MovieDetail',
  components:{
    MovieInfo,
    MovieNav,
  },
  computed: {
    ...mapGetters(['movie']),
    poster() {
      return this.movie.poster_path ? `https://image.tmdb.org/t/p/original/${ this.movie.poster_path }` : '..'
    },
  },
}
</script>

<style scoped>
#modal-header {
  text-align: right;
}
.modal-dialog {
  filter: drop-shadow(2px 4px 6px #7A7373);
}
.modal-content {
  background: #000000; 
  border-radius: 10px;
}
#modal-body {
  height:700px;
}
#poster-box {
  width:480px;
  height: 670px;
}
#poster {
  width: 100%;
  height: 100%;
  border-radius: 10px;
}
#movie-info{
  height: 305px;
}
.close-btn {
  background:transparent;
  color: #e11616;
}
</style>