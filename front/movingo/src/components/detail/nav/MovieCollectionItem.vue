<template>
  <div>
    <div class="collection-card" v-for="movie in collection.movies" :key="movie.pk">
      <div v-for="thumbnail in thumbnails" :key="thumbnail.poster_path">
        <img :src="`https://image.tmdb.org/t/p/original/${thumbnail.poster_path}`" alt="">
      </div>
    </div>
      {{ collection.title }}
  </div>
</template>
<!-- <div v-for="(n,index) for 3" :key=index>
  <p>{{list[n]}}</p>-->

<script>
export default {
  name: 'MovieCollectionItem',
  props: {
    collection: Object,
  },
  components: {
  },
  computed: {
    thumbnails() {
      const allMovies = this.collection.movies
      if (this.collection.movies.length >= 4) {
        const representMovies = allMovies.splice(4)
        return representMovies
      } else {
        return allMovies
      }
    } 
  }
}
</script>

<style scoped>
  .collection-card {
    width: 200px;
    height: 100px;
  }
  .mini-poster {
    display: absolute;
    width: 100%;
    height: 100%;
  }
</style>