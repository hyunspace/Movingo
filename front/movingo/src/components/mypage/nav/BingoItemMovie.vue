<template>
  <div>
    <div v-if="reviewed" style="position:relative" class="frame">
      <div :style="`background-image:${poster_url}`" id="reviewed-item"></div>
      <div id="review-rate"><i class="bi bi-star-fill mx-1"></i> {{ rate }}</div>  
    </div>
    <div v-if="!reviewed" style="position:relative" class="frame">
      <div :style="`background-image:${poster_url}`" id="not-reviewed-item"></div>
      <div id="not-reviewed-content"><p class="not-reviewd-title">{{ movie.title }}</p></div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: "BingoItemMovie",
  props:{
    movie:Object,
    user_pk: Number,
  },
  computed:{
    poster_url() {
      return `url(https://image.tmdb.org/t/p/original/${this.movie.poster_path})`
    },
    reviewed() {
      return this.movie.reviews.filter(element => {
        return element.user == parseInt(this.user_pk)
      }).length
    },
    rate() {
      return this.reviewed ? this.movie.reviews.filter(element => {
        return element.user == parseInt(this.user_pk)
      })[0].rate : 0
    }
  
  }
  
}
</script>

<style scoped>
/* .bingo-items {
  
} */

/* .bingo-items{
  position:relative;
  height:109.59px; 
  background-size:cover;
  border-radius: 5px;
  display:flex;
  justify-content: center;
}
.bingo-items:hover{
  filter: brightness(0.4);
}
#not-reviewed-content{
  visibility: hidden;
}
.bingo-items:content #not-reviewed-hover{
  visibility: visible;
} */

#not-reviewed-item{
  height:109.59px; 
  background-size:cover;
  border-radius: 5px;
}

#reviewed-item {
  filter: contrast(80%), saturate(80%), brightness(90%), blur(5px);
}

.frame:hover #not-reviewed-item{
  filter:brightness(0.4);
}

#not-reviewed-content{
  position:absolute;
  top:0;
  bottom:0;
  left: 0;
  right: 0;
  color:white;
  z-index: 10;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 1 0 1;
}


.frame #not-reviewed-content{
  opacity:0;
}

.frame:hover #not-reviewed-content{
  opacity:1;
}

#reviewed-item{
  height:109.59px; 
  background-size:cover;
  border-radius: 5px;
  filter:brightness(0.4);
}

#review-rate{
  position:absolute;
  color:white;
  top: 43px;
  z-index: 10;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 37px;
}

.frame:hover #reviewed-item{
  filter:brightness(1);
}


.frame:hover #review-rate{
  opacity:0;
}

.bi-star-fill {
  color:yellow;
}
</style>