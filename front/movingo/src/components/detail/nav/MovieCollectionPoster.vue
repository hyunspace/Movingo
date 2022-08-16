<template>
  <div>
    <div id="collection-poster" class="row">
      <!-- <div v-for="c_movie in pp_movies" :key="c_movie.poster_path" class="col-6 mcm-poster"> -->
        <!-- <img style="width:100%; height:100%;" :src="`https://image.tmdb.org/t/p/original/${ c_movie.poster_path }`" alt=""> -->
      <!-- </div>       -->
      <p style="margin-top:20px; padding:0;">{{ mcmtitle }}</p>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: "MovieCollectionPoster",
  props: {
    collection: Object,
  },
  computed: {
    pp_movies() {
      let collection_movies = this.collection.movies
      return collection_movies.splice(0, _.max(4, collection_movies.length) )
    },
    mcmtitle() {
      let mc_title = this.collection.title
      return mc_title.substr(0,9)+"..."
    }
  }
}
</script>

<style scoped>
#collection-poster{
  width: 170px;
  height: 230px;
  padding:10px;
  background:white;
  border-radius: 7px;
}
.mcm-poster{
  width:75px;
  height: 105px;
  padding:0px;
}
</style>