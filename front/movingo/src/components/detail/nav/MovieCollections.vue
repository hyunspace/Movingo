<template>
  <div class="d-flex justify-content-between" style="padding-left:10px; padding-right:10px; padding-top:20px;">
    <div v-for="collection in collections" :key="collection.title">
      <div id="collection-poster" class="row" @click="movetoCollection(collection.pk)" data-bs-dismiss="modal">
        <div v-for="c_movie in [...collection.movies].splice(0,4)" :key="c_movie.poster_path" class="col-6 mcm-poster">
          <img style="width:100%; height:100%;" :src="`https://image.tmdb.org/t/p/original/${ c_movie.poster_path }`" alt="">
        </div>      
        <p style="margin-top:20px; padding:0;">{{ collection.title.substr(0,9)+"..." }}</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieCollections',
  props: {
    collections:Array,
  },
  components: {

  },
  methods:{
    movetoCollection(collectionPk) {
      this.$router.push({ name:"collection_detail", params: { collectionPk: collectionPk } })
    }
  },
  computed: {


  }

}
</script>

<style scoped>
#collection-poster:hover{
  cursor: pointer;
  opacity: 0.8;
}
#collection-poster{
  width: 176px;
  height: 250px;
  padding:10px;
  background:white;
  border-radius: 7px;
}
.mcm-poster{
  width:78px;
  height: 115px;
  padding:0px;
}
</style>