import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'
// import accounts from './accounts'

export default {
    // namespaced: true,
    state: {
      movies: [],
      movie: {},
      suggests:[],
      review: {},
      reviews: [],
      trailerURI: "",
      onlyUserReview: false,
      firstReview: true,
      foundCollections: {},
    },
  
    getters: {
      movies: state => state.movies,
      movie: state => state.movie,
      // searched_movies: state => state.searched_movies,
      suggests: state => state.suggests,
      review: state => state.review,
      reviews: state => state.reviews,
      onlyUserReview: state => state.onlyUserReview,
      isFirstReview: state => state.firstReview,
      trailerURI: state => state.trailerURI,
      // isAuthor: (state, getters) => {
      //   return state.movie.user?.username === getters.currentUser.username
      // },
      isMovie: state => !_.isEmpty(state.movie),
      foundCollections: state => state.foundCollections,
    },
  
    mutations: {
      SET_MOVIES: (state, movies) => state.movies = movies,
      SET_MOVIE: (state, movie) => state.movie = movie,
      SET_SUGGESTS: (state, suggests) => state.suggests = suggests,
      SET_REVIEW: (state, review) => state.review = review,
      SET_REVIEWS: (state, reviews) => state.reviews = reviews,
      SET_trailerURI: (state, trailerURI) => state.trailerURI = trailerURI,
      SET_MOVIE_REVIEWS: (state, reviews) => (state.reviews = reviews),
      SET_ONLY_USER_REVIEW: state => (state.onlyUserReview = !state.onlyUserReview),
      SET_IS_FIRST: (state, firstReview) => state.isFirstReview = firstReview,
      SET_MOVIE_COLLECTIONS: (state, foundCollections) => state.foundCollections = foundCollections
    },
  
    actions: {
      fetchMovies({ commit, getters }, keyword) {
        /* 게시글 목록 받아오기
        GET: articles URL (token)
          성공하면
            응답으로 받은 게시글들을 state.articles에 저장
          실패하면
            에러 메시지 표시
        */
        let query = "?"
        if (keyword) {
          query += `keyword=${keyword}`
        }

        axios({
          url: drf.movies.movies()+query,
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            console.log(res.data)
            commit(`SET_MOVIES`, res.data)
          })
          .catch(err => console.error(err.response))
      },

      fetchMovie({ commit, getters }, moviePk) {
        /* 영화 정보 1개 받아오기
        GET: article URL (token)
          성공하면
            응답으로 받은 정보를 state.movie에 저장
          실패하면
            단순 에러일 때는
              에러 메시지 표시
            404 에러일 때는
              NotFound404 로 이동
        */
        axios({
          url: drf.movies.movie(moviePk),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            console.log(res.data)
            commit('SET_MOVIE', res.data)
          })
            
          .catch(err => {
            console.error(err.response)
            if (err.response.status === 404) {
              router.push({ name: 'NotFound404' })
            }
          })
      },

      fetchTrailerURI({ commit }, keyword) {
        /* 예고편 받아오기
        GET: 유튜브 API
          성공하면
            응답으로 받은 영상을 state.trailerURI에 저장
          실패하면
            에러 메시지 표시
        */

        // const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
        const API_URL = 'https://www.googleapis.com/youtube/v3/search'
        commit('SET_trailerURI', '')
        const params = {
            part: 'snippet',
            type: 'video',
            key: '',
            q: keyword + ' official trailer',
          }
        axios.get(API_URL,{params})
        .then(res => {
          commit('SET_trailerURI', `https://www.youtube.com/embed/${res.data.items[0].id.videoId}`)
        })
        .catch(err => {
          console.log(err)
        })
      },
      
      wishMovie({ commit, getters }, moviePk) {
        axios({
          url: drf.movies.wishMovie(moviePk),
          method: 'post',
          headers: getters.authHeader,
        })
        .then(res => {
          commit('SET_MOVIE', res.data)
        })
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
      },

      fetchReview({ commit, getters }, { moviePk, reviewPk }) {
        /* 특정 영화에서 특정 유저가 쓴 리뷰 1개만 가져오기 */
        console.log(moviePk, reviewPk)
        axios({
          url: drf.movies.likeUpDeReview(moviePk, reviewPk),
          method: 'get',
          headers: getters.authHeader,
        })
        .then(res => {
          commit('SET_REVIEW', res.data)
        }) 
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
      },
      
      createReview({ commit, getters }, { moviePk, rate, content}) {
        /* 리뷰 생성(등록)
        POST: 
          성공하면
            응답으로 state.reviews의 reviews 갱신해서 보여주기
          실패하면
            에러 메시지 표시
        */
       axios({
         url: drf.movies.review(moviePk),
         method: 'post',
         data: { rate, content },
         headers: getters.authHeader,
       })
          .then(res => {
            commit('SET_MOVIE', res.data)  
          })
          .catch(err => 
            { if (err.response.data.content && err.response.data.rate) {
              alert('별점과 리뷰를 입력해주세요')
              console.err(err.response)
            } else if (err.response.data.content) {
              alert('리뷰를 입력해주세요')
              console.err(err.response)
            } else {
              alert('별점을 입력해주세요')
              console.err(err.response)
            }  
          })
        },

      likeReview({ commit, getters }, { moviePk, reviewPk }){
        axios({
          url: drf.movies.likeUpDeReview(moviePk, reviewPk),
          method: 'post',
          headers: getters.authHeader,
        })
        .then(res => {
          console.log('axios 성공')
          commit('SET_MOVIE', res.data)
        })
        .catch(err => console.error(err.response))
      },

      switchUserReview({ commit }, { moviePk, reviewPk }) {
        console.log(moviePk, reviewPk)
        commit('SET_ONLY_USER_REVIEW')
      },

      updateReview({ commit, getters }, { moviePk, reviewPk, rate, content }){
        const review = { rate, content }
        axios({
          url: drf.movies.likeUpDeReview(moviePk, reviewPk),
          method: 'put',
          data: review,
          headers: getters.authHeader,
        })
        .then(res => {
          commit('SET_MOVIE', res.data)
        })
        .catch(err => 
          { if (err.response.data.content && err.response.data.rate) {
            alert('별점과 리뷰를 입력해주세요')
            console.err(err.response)
          } else if (err.response.data.content) {
            alert('리뷰를 입력해주세요')
            console.err(err.response)
          } else {
            alert('별점을 입력해주세요')
            console.err(err.response)
          }
        })
      },

      deleteReview({ commit, getters }, { moviePk, reviewPk }){
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.movies.likeUpDeReview(moviePk, reviewPk),
            method: 'delete',
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_MOVIE', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },

      autoComplete({ commit, getters }, keyword) {
        commit('SET_SUGGESTS', [])
        axios({
          url: drf.movies.auto_complete(keyword),
          method: 'get',
          headers: getters.authHeader,
        })
        .then(res => {
          commit('SET_SUGGESTS', res.data)
        })
      },

      deleteSuggestion({ commit }) {
        commit('SET_SUGGESTS', [])
      },

      lookForCollections({ commit, getters }, moviePk) {
        axios({
          url: drf.movies.lookForCollections(moviePk),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_MOVIE_COLLECTIONS', res.data)
          })
          .catch(err => console.error(err.response))
      }
  }
}