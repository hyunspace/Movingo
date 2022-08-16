<template>
  <div id="collection-detail">
    <div class="d-flex align-items-center">
      <h2 id="collection-title">{{ collection.title }}</h2>
      <span id="collection-maker" v-if="collection.user">by <span id="maker-nickname" @click="movetoProfile()">{{ collection.user.profile_info[0].nickname }}</span></span>
    </div>
    <div class="row my-4">
      <div class="col-6 px-3">
        <div id="collection-img-background">
          <img v-if="collection.movies" :src="backdrop_path" style="width:100%; height:100%; border-radius:10px;" alt="">
        </div>
      </div>
      <div class="col-6">
        <div>
          <div id="description">
            <h5>소개글</h5>
            <p class="description">{{ collection.description }}</p>
            <div v-if="liked" class="d-flex">
              <button class="like-button" @click="likeCollection(collection.pk)"><i class="ilike bi bi-heart-fill"></i></button>
              <p class="like-cnt">{{ like_cnt }}</p>
            </div>
            <div v-if="!liked" class="d-flex">
              <button class="like-button" @click="likeCollection(collection.pk)"><i class="ilike bi bi-heart"></i></button>
              <p class="like-cnt">{{ like_cnt }}</p>
            </div>
          </div>
        </div>
        <div id="buttons" v-if="collection.user.pk == currentUser.pk">
          <div class="d-flex justify-content-end" >
            <button data-bs-toggle="modal" data-bs-target="#createcollection" class="btn update-btn">수정</button> 
            <button @click="checkDelete(collection.pk)" class="btn delete-btn">삭제</button>
          </div>
        </div>
      </div>
    </div>
    <div id="movies-list-background">
      <movies-list :movies="collection.movies"></movies-list>
    </div>
    <collection-creation-form v-if="isCollection" :formCollection="formC" action="update"></collection-creation-form>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import CollectionCreationForm from '@/components/collections/CollectionCreationForm.vue';
import MoviesList from '@/components/MoviesList'
export default {
  name: "CollectionDetail",
  data() {
    return {
      collectionPk: this.$route.params.collectionPk,
    }
  },
  components: {
    MoviesList, CollectionCreationForm,
  },
  computed: {
    ...mapGetters(['collection','currentUser']),
    like_cnt() {
      return this.collection.like_users_cnt
    },
    liked() {
      return this.collection.like_users_cnt ? this.collection.like_users.filter(element => {
        return element.pk == this.currentUser.pk
      }) .length : false
    },
    description() {
      return String(this.collection.description).substr(0, 30)
    },
    backdrop_path() {
      return  this.collection.movies ? 'https://image.tmdb.org/t/p/original' + this.collection.movies[0].backdrop_path : "../assets/logo.png"
      // + this.collection.movies['0'].backdrop_path
    },
    isCollection(){
      return this.collection.pk ? true : false;
    },
    formC() {
      return {
        pk: this.collection.pk,
        title: this.collection.title,
        description: this.collection.description,
        movies: this.collection.movies,
      }
    }
  },
  methods: {
    ...mapActions(['fetchCollection', 'likeCollection', 'deleteCollection']),
    checkDelete(pk){
      if (confirm('정말 이 컬렉션을 삭제하시겠습니까?')){
        this.deleteCollection(pk)
      }
    },
    movetoProfile() {
      this.$router.push({name: 'profile', params: { username: this.collection.user.username }})
    }
    
  },
  created() {
    this.fetchCollection(this.collectionPk)
  }
}
</script>

<style scoped>
#collection-detail{
  margin:50px;
  color: white;
}
#collection-title{
  font-weight:600;
  font-size:30px;
  line-height:36px;
}
#collection-maker{
  margin-left: 10px;
}
#collection-maker:hover {
  cursor: pointer;
}
#collection-img-background{
  width:100%;
  height:400px;
  border-radius: 10px;
  background:#36393F;
}
#collection-img{
  width: 100%;
  height: 100%;
  border:none;
  border-radius: 10px;
}
h4{
  font-size:24px;
}
#description {
  height: 300px;
  padding: 15px;
  margin-bottom: 10px;
  font-size: 16px;
}
.description {
  font-size: 16px;
  margin-bottom: 15px;
}
#buttons {
  margin-right: 20px;
}
.like-button {
  background: black;
  border:none;
  color:white;
  padding:0;
}
.like-cnt {
  margin: 6px 0 0 8px;
}
.ilike {
  color:#e11616;
  font-size: 25px;
}
#movies-list-background{
  background:#36393F;
    width:100%;
    height:326px;
    margin-top:100px;
    border-radius: 10px;
}
.update-btn {
  background-color: #36393f;
  border-radius: 6px;
  color: #ffffff;
  width: 15%;
  height: 2.5rem;
  margin-right: 0.5rem;
}
.delete-btn {
  background-color: #e1161e;
  border-radius: 6px;
  color: #ffffff;
  width: 15%;
  height: 2.5rem;
}
.modify-btn:hover {
  border-bottom:solid 1px #eee;
  color:white;
}

</style>