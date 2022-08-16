<template>
  <router-link class="collection-card-router" :to="{ name: 'collection_detail', params: { collectionPk : collection.pk } }">
    <div id="collection-card">
      <div id="collection-background">
        <img v-if="collection.movies.length" :src="backdrop_path" style="width:100%; height:100%; border-top-left-radius: 10px; border-top-right-radius: 10px;" alt="">
        <div id="collection-user-profile" style="border:none;">
          <img v-if="user_img == 1" style="height:100%; width:100%;" src="@/assets/KDW.png" alt="">
          <img v-if="user_img == 2" style="height:100%; width:100%;" src="@/assets/OHM.png" alt="">
          <img v-if="user_img == 3" style="height:100%; width:100%;" src="@/assets/KJH.png" alt="">
          <img v-if="user_img == 4" style="height:100%; width:100%;" src="@/assets/KHG.png" alt="">
          <img v-if="user_img == 5" style="height:100%; width:100%;" src="@/assets/KNR.png" alt="">
          <img v-if="user_img == 6" style="height:100%; width:100%;" src="@/assets/KHR.png" alt="">
        </div>
      </div>
      <div id="collection-card-info">
        <h5 id="collection-card-title">{{ title }}</h5>
        <div class="d-flex justify-content-between">
          <p id="collection-user">by {{ collection.user.profile_info[0].nickname }}</p>
        </div>
        <div>
          <div v-if="liked">
            <button><i class="collectioncardlike bi bi-heart-fill"></i></button>
            <span class="mx-2">{{ like_cnt }}</span>
          </div>
          <div v-if="!liked">
            <button><i class="collectioncardlike bi bi-heart"></i></button>
            <span class="mx-2">{{ like_cnt }}</span>
          </div>
        </div>
        <div id="collection-description">{{ description }}</div>
      
      </div>
    </div>
  </router-link>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'CollectionCard',
  props: {
    collection:Object
  },

  components: {
  },
  computed: {
    ...mapGetters(['currentUser']),
    title() {
      return this.collection.title.length > 13 ? String(this.collection.title).substr(0, 13) +'...' : this.collection.title
    },
    like_cnt() {
      return this.collection.like_cnt
    },
    liked() {
      return this.collection.like_users.filter(element => {
        return element.id == this.currentUser.pk
      }).length
    },
    description() {
      return String(this.collection.description).substr(0, 30)
    },
    backdrop_path() {
      return  this.collection.movies ? 'https://image.tmdb.org/t/p/original' + this.collection.movies[0].backdrop_path : "../assets/logo.png"
      // + this.collection.movies['0'].backdrop_path
    },
    user_img(){
      return this.collection.user.profile_info[0].profile_img
    }
  },
}
</script>

<style scoped>

.collection-card-router {
  text-decoration: none;
}
.collection-card-router:hover{
  opacity: 0.8;
}
#collection-card {
  font-family: 'Pretendard';
  width:100%;
  height: 400px;
  /* border:solid 1px ; */
  border-radius: 10px;
  color: black; 
  border: 1px solid rgba(255, 255, 255, 0.5);
  filter: drop-shadow(0 0 2px #ffffff);
  /* box-shadow: 2px 2px 5px rgba(255, 255, 255, 0.5); */
}
#collection-background {
  position:relative;
  background: #36363f;
  width: 100%;
  height: 12rem;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}
#collection-user-profile {
  border:  2.5px solid #ffffff;
  position: absolute;
  overflow: hidden;
  background: #36363f;
  top: 157px;
  left: 36.7%;
  width: 5rem;
  height: 5rem;
  border-radius: 100%;
  box-shadow: 2px 2px 3px rgba(0, 0, 0, 0.25);
}
#collection-user {
  font-weight:500;
  color: #40444b;
}
#collection-card-info {
  padding-top:60px;
  padding-left:20px;
  padding-right:20px;
  background: #ffffff;
  height: 208px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}
#collection-title {
  margin:0px;
  font-size:20px;
  font-weight: 700;
}
.collection-tag {
  padding:1px;
  padding-left:3px;
  padding-right:3px;
  border-radius:3px;
  
  background:#40444b;
  font-size: 10px;
  color:#FFFFFF;
}
#collection-card-description{
  margin-top:8px;
}
button {
  background: #ffffff;
  border:none;
  padding:0;
}
.collectioncardlike {
  color:#e11616;
}

</style>
