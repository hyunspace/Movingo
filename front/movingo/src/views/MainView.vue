<template>
  <div>
    <main-carousel></main-carousel>
    <br><br><br>
    <div v-if="isLoggedIn">
      <div v-for="main_collection in main_collections" :key= main_collection.pk>
        <movies-list :movielisttitle="`${main_collection.title}`" :movies="main_collection.movies"></movies-list>
      </div>
    </div>
  </div>
  
</template>

<script>
import MainCarousel from '@/components/MainCarousel'
import MoviesList from '@/components/MoviesList'
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'MainView',
  components: {
    MainCarousel,
    MoviesList,
  },
  computed: {
    ...mapGetters(['main_collections', 'isLoggedIn'])
  },
  methods: {
    ...mapActions(['fetchMainCollections'])
  },
  created() {
    if (this.isLoggedIn) {
    this.fetchMainCollections()
    }
  },
}
</script>
<style scoped>
h1{
  color:whilte;
}
li {
  color:black;
}
</style>
