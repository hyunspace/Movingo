<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <div id="overview_bingo" class="row row-cols-5 mx-1 my-3">
          <div v-for="bingo_movie in currentBingo.movies" :key="bingo_movie.pk" class="bingo-movies col" style="height:109.59px">          
            <bingo-item-movie :movie="bingo_movie" :user_pk="profile.pk"></bingo-item-movie>
          </div>
        </div>
      </div>
      <div class="col my-3">
        <div>
          <div v-if="mostViewed" class="row">
            <div id="overview_analysis" class="col mx-1 px-3">
              <div class="gerne-noti">
                <p style="font-size: 20px;"><span style="font-size:24; font-weight:600;">{{ profile.profile_info[0].nickname }}</span>님은</p>
                <span class="the-genre">{{ mostViewed }}</span>
                <p style="font-size: 20px;">장르의 영화를</p>
                <p style="font-size: 20px;">가장 많이 봤어요!</p>
               </div>
            </div>  
            <div id="overview_chart" class="col mx-1 px-3">
              <pie-chart style="height:100%; width:100%" :genreNames="genreNames" :genreTimes="genreTimes"></pie-chart>
            </div>
          </div>
          <div v-else style="margin:0;">
            <div id="overview_analysis" class="col px-3 d-flex flex-column justify-content-center text-center" style="margin:0; width:100%">
              <p>아직 작성한 리뷰가 없어요</p>
              <p>리뷰를 남기면 취향을 알려드릴게요!</p>
            </div>
          </div>
        </div>
        <div id="overview-recent-review" class="col mx-1 my-2">
          <h5 v-if="recentReview" class="recent-review">가장 최근에 작성한 리뷰예요</h5>
          <div v-if="recentReview" id="recent-review-card">
            <div class="row">
              <div class="col-4" >
                <img :src="`https://image.tmdb.org/t/p/original/${recentReview.movie.poster_path}`" alt="" class="recent-review-poster">
              </div>
              <div class="col-8 review-card">
                <div class="review-header d-flex justify-content-between">
                  <h5 class="recent-review-title">{{ recentReview.movie.title }}</h5>
                  <p class="recent-review-rate"><i class="bi bi-star-fill"></i> {{ recentReview.rate }}</p> 
                </div>
                <div class="recent-review-genres d-flex">
                  <div v-for="genre in recentReview.movie.genres" :key="genre.id" >
                    <span v-if="genre.name=='모험'" class="adventure">{{ genre.name }}</span>
                    <span v-if="genre.name=='판타지'" class="fantasy">{{ genre.name }}</span>
                    <span v-if="genre.name=='애니메이션'" class="animation">{{ genre.name }}</span>
                    <span v-if="genre.name=='드라마'" class="drama">{{ genre.name }}</span>
                    <span v-if="genre.name=='공포'" class="horror">{{ genre.name }}</span>
                    <span v-if="genre.name=='액션'" class="action">{{ genre.name }}</span>
                    <span v-if="genre.name=='코미디'" class="comedy">{{ genre.name }}</span>
                    <span v-if="genre.name=='역사'" class="history">{{ genre.name }}</span>
                    <span v-if="genre.name=='서부'" class="western">{{ genre.name }}</span>
                    <span v-if="genre.name=='스릴러'" class="thriller">{{ genre.name }}</span>
                    <span v-if="genre.name=='범죄'" class="crime">{{ genre.name }}</span>
                    <span v-if="genre.name=='다큐멘터리'" class="documentary">{{ genre.name }}</span>
                    <span v-if="genre.name=='SF'" class="sf">{{ genre.name }}</span>
                    <span v-if="genre.name=='미스터리'" class="mystery">{{ genre.name }}</span>
                    <span v-if="genre.name=='음악'" class="music">{{ genre.name }}</span>
                    <span v-if="genre.name=='로맨스'" class="romance">{{ genre.name }}</span>
                    <span v-if="genre.name=='가족'" class="family">{{ genre.name }}</span>
                    <span v-if="genre.name=='전쟁'" class="war">{{ genre.name }}</span>
                    <span v-if="genre.name=='TV 영화'" class="tvshow">{{ genre.name }}</span>
                  </div>
                </div>
                <hr>
                <div class="recent-review-content">
                  <p>{{ recentReview.content }}</p>
                </div>
                <hr>
                <div class="extra d-flex justify-content-between">
                  <p class="like-text">좋아요 {{ recentReview.like_users_cnt }}개</p>
                </div>
              </div>
            </div>
          </div>
          <div v-if="!recentReview" class="text-center">
            <h5 class="sorry-no-review">아직 작성한 리뷰가 없어요</h5>
          </div>      
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BingoItemMovie from './BingoItemMovie'
// import RadarChart from './RadarChart'
import PieChart from './PieChart'
import { mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  name:'ProfileOverview',
  props: {
    profile:Object,
  },
  computed: {
    ...mapGetters(['currentBingo','currentUser']),
    ordered_collections() {
      return [...this.profile.collections].sort(function(a, b) {
        return a.like_users_cnt > b.like_users_cnt ? -1 : a.like_users_cnt < b.like_users_cnt ? 1 : 0;
      }).splice(0, 2)
    },
    Genres() {
      let result = {}
      this.profile.reviews.forEach(element => {
        element.movie.genres.forEach(e => {
         if (e.name in result) {
          result[`${e.name}`] += 1
         } else {
           result[`${e.name}`] = 1
         }
        })
      });
      console.log(result)
      return result
    },
    genreNames() {
      let names = Object.keys(this.Genres)
      return names
    },
    genreTimes() {
      let times = Object.values(this.Genres)
      return times
    },
    mostViewed() {
      let index = this.genreTimes.indexOf(_.max(this.genreTimes))
      return Array(...this.genreNames)[index]
    },
    recentReviewPk() {
      const mostRecentReview = this.profile.reviews ? this.profile.reviews.length : 1
      return mostRecentReview - 1
    },
    recentReview() {
      return this.profile.reviews ? this.profile.reviews[this.recentReviewPk] : false
    }
    
  },
  components:{
    BingoItemMovie,
    PieChart
  }
}
</script>

<style scoped>
.container {
  margin-top: 10px;
}
#overview_bingo { 
  width: 38rem;
  height: 38rem;
  border-radius: 10px;
  background: #ffffff;
}
#overview_analysis { 
  width: 25rem;
  height: 18.65rem;
  border-radius: 10px;
  background: #000000;
  font-size: 20px;
}
#overview_chart { 
  width: 25rem;
  height: 18.65rem;
  border-radius: 10px;
  background-color: #000000;
}
#overview-recent-review{
  width: 32.7rem;
  height: 18.75rem;
  border-radius: 10px;
  background: #36393f;
  padding: 0.5rem 0.8rem 0.5rem 0.8rem;
}
#recent-review-card{
  background: #ffffff;
  border-radius: 5px;
  height: 223px;
  padding: 0.7rem;
  color: #36393f;
}
.recent-review-poster {
  width:150px;
  height:208px;
  border-radius:7px;
}
.recent-review-title {
  padding-top: 4px;
  padding-bottom: 4px;
  font-weight: bold;
}
.recent-review-rate {
  margin: 5px 10px 0 0;
}
.bi-star-fill {
  color: gold;
}
hr {
  margin-right: 10px;
  margin-bottom: 7px;
}
.bingo-movies {
  padding:6px;
  border-radius: 5px;
}
.gerne-noti {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.the-genre {
  color: #e11616; 
  font-weight: bold; 
  font-size: 30px;
}
.recent-review {
  margin: 10px 0 10px 5px;
  color: #ffffff;
}
.recent-review-content {
  height: 70px;
}
.sorry-no-review {
  margin-top: 125px;
}
/* genre color */
  .adventure {
    border-radius: 7px;
    background: #e76f51;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .fantasy {
    border-radius: 7px;
    background: #5e548e;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .animation {
    border-radius: 7px;
    background: #fcbf49;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .drama {
    border-radius: 7px;
    background: #ffb5a7;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .horror {
    border-radius: 7px;
    background: #6a040f;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .action {
    border-radius: 7px;
    background: #c1121f;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .comedy {
    border-radius: 7px;
    background: #8ac926;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .history {
    border-radius: 7px;
    background: #52796f;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .western {
    border-radius: 7px;
    background: #432818;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .thriller {
    border-radius: 7px;
    background: #bc4749;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .crime {
    border-radius: 7px;
    background: #001233;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .documentary {
    border-radius: 7px;
    background: #619b8a;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .sf {
    border-radius: 7px;
    background: #480ca8;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .mistery {
    border-radius: 7px;
    background: #33415c;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .music {
    border-radius: 7px;
    background: #5fa8d3;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .romance {
    border-radius: 7px;
    background: #ffb3c6;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .family {
    border-radius: 7px;
    background: #ffd166;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .war {
    border-radius: 7px;
    background: #370617;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
  .tvshow {
    border-radius: 7px;
    background: #00bbf9;
    color: #ffffff;
    padding:5px;
    margin-right: 7px;
  }
</style>


