import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'
// import router from '@/router'

// import _ from 'lodash'
// import accounts from './accounts'



export default {
  // namespaced: true,
  

  state: {
    threads: {},
    thread: {},
    movieThread: {},
  },

  getters: {
    threads: state => state.threads,
    thread: state => state.thread,
    movieThread: state => state.movieThread,
  },

  mutations: {
    SET_THREADS: (state, threads) => state.threads = threads,
    SET_THREAD: (state, thread) => state.thread = thread,
    SET_THREAD_EXISTS: (state, movieThread) => state.movieThread = movieThread
  },

  actions: {
    fetchThreads({ commit, getters }) {
      commit('SET_THREADS', [])

      axios({
        url: drf.community.community_list(),
        method:'get',
        headers: getters.authHeader, 
      })
      .then(res => {
        commit('SET_THREADS', res.data)
      })
      .catch(err => console.error(err.response))
    },

    fetchThread({ commit, getters }, threadPk) {
      commit('SET_THREADS', [])

      axios({
        url: drf.community.thread_detail(threadPk),
        method:'get',
        headers: getters.authHeader, 
      })
      .then(res => {
        commit('SET_THREAD', res.data)
      })
      .catch(err => console.error(err.response))
    },

    createThread({ getters }, moviePk) {

      axios({
        url: drf.community.create_thread(moviePk),
        method:'post',
        headers: getters.authHeader, 
      })
      .then(res => {
        router.push({ name: 'community_detail', params: { threadPk:res.data.pk } })
      })
      .catch(err => console.error(err.response))
    },

    movetoThread({ getters }, moviePk) {

      axios({
        url: drf.community.create_thread(moviePk),
        method:'post',
        headers: getters.authHeader, 
      })
      .then(res => {
        router.push({ name: 'community_detail', params: { threadPk:res.data.pk } })
      })
      .catch(err => console.error(err.response))
    },

    createComment({ commit, getters }, { threadPk, newcomment }) {
      axios({
        url: drf.community.create_comment(threadPk),
        data: newcomment,
        method:'POST',
        headers: getters.authHeader, 
      })
      .then(res => {
        commit('SET_THREAD', res.data)
      })
      .catch(err => console.error(err.response))
    },

    deleteComment({ commit, getters }, { threadPk, commentPk }) {
      axios({
        url: drf.community.delete_comment(threadPk, commentPk),
        method:'delete',
        headers: getters.authHeader, 
      })
      .then(res => {
        commit('SET_THREAD', res.data)
      })
      .catch(err => console.error(err.response))
    },

    lookForThread({ commit, getters }, moviePk) {
      axios({
        url: drf.community.checkThread(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        console.log('axios 요청 성공! thread를 붙입시다')
        console.log(res.data)
        commit('SET_THREAD_EXISTS', res.data)
      })
      .catch(err => {
        console.log('에러났음')
        console.error(err.response)
      }
        )
    }
  }
}
  