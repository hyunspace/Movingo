<template>
  <div id="user-collections" class="mx-1 my-3">
    <h3>{{ nickname }} 님의 컬렉션</h3>
    <div v-for="collection in collections" :key="collection.pk" class="user-collection">
      <div class="d-flex justify-content-between align-items-end">
        <h4>{{ collection.title }}</h4>
        <span class="seemore" @click="gotoCollectionDetail(collection.pk)">자세히 보기></span>
      </div>
      <div class="collectionlists" v-if="collection.movies">
        <movies-list :movies="collection.movies"></movies-list>
      </div>
    </div>
    <movie-detail></movie-detail>
  </div>
</template>

<script>
import MoviesList from '@/components/MoviesList'
import MovieDetail from '@/components/detail/MovieDetail'
import { mapActions } from 'vuex'
export default {
  name:'UserCollections',
  props: {
    collections:Array,
    nickname:String,
  },
  components:{
    MoviesList,
    MovieDetail
  },
  methods: {
    ...mapActions(['createThread']),
    gotoCollectionDetail(collectionPk) {
      this.$router.push({name: 'collection_detail', params: { collectionPk: collectionPk }})
    }
  }
}
</script>

<style scoped>
.user-collection > .collectionlists{
  width: 100%;
  border-radius: 10px;
  background: #36393f;
}
.empty_collection {
  width: 100%;
  border-radius: 10px;
  background: #36393f;
}
h3{
  margin-top: 20px;
  margin-bottom: 25px;
  font-weight: bold;
}
.seemore:hover{
  cursor: pointer;
  opacity:0.8;
}
</style>