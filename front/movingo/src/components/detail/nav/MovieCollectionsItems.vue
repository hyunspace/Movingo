<template>
  <div>
    <div class="collection-container">
      <movie-collection-item
        v-for="collection in collections" :key="collection.pk"
      :collection="collection"></movie-collection-item>  
    </div>
  </div>
</template>

<script>
import MovieCollectionItem from './MovieCollectionItem'

export default {
  name: 'MovieCollectionItems',
  props: {
    collections: Array,
  },
  components: {
    MovieCollectionItem,
  }
}
</script>

<style scoped>
.collection-container{
  width: 100%;
  height: 100%;
}
</style>