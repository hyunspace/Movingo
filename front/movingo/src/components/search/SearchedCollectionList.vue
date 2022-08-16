<template>
  <div class="row">
    <carousel id="mlc" :perPage=4 :scrollPerPage="false" :navigationEnabled="true" :paginationEnabled="false">
      <slide id="movie-list-slide" class="label mx-0" v-for="collection in collections" :key="collection.pk">   
        <collection-card :collection="collection" ></collection-card>
      </slide>
    </carousel>
    <!-- <div v-for="collection in collections" :key="collection.pk" class="col-6 searched-collection-card">
      <collection-card :collection="collection" ></collection-card>
    </div> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { Carousel, Slide } from 'vue-carousel'
import CollectionCard from '@/components/collections/CollectionCard'
export default {
  name: "SearchedMovieList",
  components: {
    CollectionCard, Carousel, Slide,
  },
  computed: {
    ...mapGetters(['collections'])
  }
}
</script>

<style scoped>
.searched-collection-card{
  margin-bottom:20px;
}

</style>
