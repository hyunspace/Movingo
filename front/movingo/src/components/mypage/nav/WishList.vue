<template>
  <div class="my-3 mx-1">
    <h3>{{ username }} 님의 위시리스트</h3>
    <div class="row">
      <div v-for="movie in movies" :key="movie.id" class="col-2">
        <movie-item :movie="movie" data-bs-toggle="modal" data-bs-target="#movieDetail"></movie-item>
      </div>
    </div>
    <movie-detail></movie-detail>
  </div>
</template>

<script>
import MovieItem from '@/components/search/SearchedMovieItem'
import MovieDetail from '@/components/detail/MovieDetail'
export default {
  name:'WishList',
  props: {
    movies:Array,
    username:String,
  },
  components:{
    MovieItem,
    MovieDetail,

  }

}
</script>

<style scoped>
#wish-list {
  width: 100%;
  border-radius: 10px;  
  background: #36393f;
}
h3{
  margin-top:20px;
  margin-bottom:15px;
  font-weight: bold;
}

</style>