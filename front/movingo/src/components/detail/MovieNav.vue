<template>
  <div id="movie-nav">
    <nav class="my-2">
      <div class="nav nav-tabs d-flex justify-content-center" id="nav-tab" role="tablist">
        <button class="nav-link active" id="nav-trailer-tab" data-bs-toggle="tab" data-bs-target="#nav-trailer" type="button" role="tab" aria-controls="nav-home" aria-selected="true">예고편</button>
        <button class="nav-link" id="nav-review-tab" data-bs-toggle="tab" data-bs-target="#nav-review" type="button" role="tab" aria-controls="nav-profile" aria-selected="false">리뷰</button>
        <button class="nav-link" id="nav-collection-tab" data-bs-toggle="tab" data-bs-target="#nav-collection" type="button" role="tab" aria-controls="nav-contact" aria-selected="false">컬렉션</button>
      </div>
    </nav>
    <div class="tab-content" id="nav-tabContent">
      <div class="tab-pane fade show active" id="nav-trailer" role="tabpanel" aria-labelledby="nav-trailer-tab">
        <movie-trailer></movie-trailer>
      </div>
      <div class="tab-pane fade active" id="nav-review" role="tabpanel" aria-labelledby="nav-review-tab">
        <movie-reviews :movie="movie"></movie-reviews>
      </div>
      <div class="tab-pane fade active" id="nav-collection" role="tabpanel" aria-labelledby="nav-collection-tab">
        <movie-collections :collections="movie_collections"></movie-collections>
      </div>
    </div>
  </div>
</template>

<script>

import MovieTrailer from './nav/MovieTrailer'
import MovieReviews from './nav/MovieReviews'
import MovieCollections from './nav/MovieCollections'

export default {
  name: 'MovieNav',
  props:{
    movie:Object,
  },
  components: {
    MovieTrailer,
    MovieReviews,
    MovieCollections,
  },
  computed: {
    movie_collections() {
      let v = this.movie.collections
      return this.movie.collections ? v.slice(0,3) : []
    }
  }
}
</script>

<style scoped>
#movie-nav{ 
  color:white;
}
.nav-link {
  color:white;
  background: none;
  border:none;
  margin-left:15px;
  margin-right:15px;
}
.nav-link:hover {
  font-weight: bold;
  border: none;
}
.active {
  font-weight: bold;
}
.tab-pane {
  color:white
}
</style>