<template>
  <div id="collection-view-all" class="row">
    <div class="d-flex justify-content-between">
      <div class="d-flex px-2">
        <h2 id="collection-view-today">{{ today }}, 오늘의 컬렉션</h2>
        <!-- Button trigger modal -->
        <button id="createnewcollection-btn" type="button" class="btn text-center py-0 mx-5" data-bs-toggle="modal" data-bs-target="#createcollection">
          <p>새 컬렉션</p>
        </button>
      </div>
      <div style="color:white;" class="d-flex align-items-end">
        <button @click="fetchCollectionsOrderBy('')" style="color:white;" class="collections-order-btn mx-1">좋아요 순</button><span style="font-size:18px;">|</span>
        <button @click="fetchCollectionsOrderBy('moviesnumber')" style="color:white;" class="collections-order-btn mx-1">영화 많은 순</button><span style="font-size:18px;">|</span>
        <button @click="fetchCollectionsOrderBy('createddate')" style="color:white;" class="collections-order-btn mx-1">최신 순</button>
      </div>
    </div>
    <div v-for="collection in collections" :key='collection.pk' class="col-3 mx-0 my-3">
      <collection-card class="collection-card" :collection="collection"> </collection-card>
    </div>
    
    <collection-creation-form :formCollection="formCollection" action="create"></collection-creation-form>
  </div>
</template>

<script>
import CollectionCard from '@/components/collections/CollectionCard'
import CollectionCreationForm from '@/components/collections/CollectionCreationForm.vue';
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MainView',
  data() {
    return {
      formCollection: {
        id: null,
        title: "",
        description: "",
        movies: [],
      }
    }
  },
  components: {
    CollectionCard,
    CollectionCreationForm,
  },
  computed: {
    ...mapGetters(['collections']),
    today() {
      let date = new Date();

      let month = ('0' + (date.getMonth() + 1)).slice(-2);
      let day = ('0' + date.getDate()).slice(-2);
      return month+ '월 '+ day+'일'
    }
  },
  methods: {
    ...mapActions(['fetchCollections', 'fetchCollectionsOrderBy']),

  },
  created() {
    this.fetchCollections()
  },
}
</script>
<style scoped>
#collection-view-all{
  margin-top:80px;
}
#createnewcollection-btn{
  background: #E11616;
  color: white;
  font-weight: 500;
  font-size:20px;
  width:130px;
  height:35px;
  margin-top: 3px;
}
#collection-view-today{
  color: white;
  font-weight: 800;
}
h1{
  color:whilte;
}
li {
  color:black;
}
.collections-order-btn {
  background:none;
  margin-bottom:0;
  border: none;
  padding-bottom:0;
}

</style>
