import axios from 'axios'
import drf from '@/api/drf'
export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
    currentBingo: {},
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    currentBingo: state => state.currentBingo

  },

  mutations: {
    SET_CURRENTBINGO: (state, bingo) => state.currentBingo = bingo

  },

  actions: {
    fetchCurrentBingo({ commit, getters }) {
    
      axios({
        url: drf.bingos.current_bingo(),
        method:'get',
        headers: getters.authHeader, 
      })
      .then(res => {
        console.log(res.data)
        commit('SET_CURRENTBINGO', res.data)
      })
      .catch(err => console.error(err.response))
    },

  }
}
