import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'
// import router from '@/router'

// import _ from 'lodash'
// import accounts from './accounts'



export default {
    // namespaced: true,
    state: {
      main_collections: [],
      collections: [],
      collection: {},
    },
  
    getters: {
      main_collections: state => state.main_collections,
      collections: state => state.collections,
      collection: state => state.collection,

    },
  
    mutations: {
      SET_MAIN_COLLECTIONS: (state, collections) => state.main_collections = collections,
      SET_COLLECTIONS: (state, collections) => state.collections = collections,
      SET_COLLECTION: (state, collection) => state.collection = collection,
    },
  
    actions: {
      fetchMainCollections({ commit, getters }) {
        // Main 페이지 컬렉션 받아오기
        commit('SET_MAIN_COLLECTIONS', [])
        axios({
          url: drf.collections.main_collections(),
          method: 'get',
          headers: getters.authHeader,
        })
        .then(res => {
          commit('SET_MAIN_COLLECTIONS', res.data)
        })
        .catch(err => console.error(err.response))
      },

        
      fetchCollections({ commit, getters }) {
        commit('SET_COLLECTIONS', [])

        axios({
          url: drf.collections.collection_list(),
          method:'get',
          headers: getters.authHeader, 
        })
        .then(res => {
          commit('SET_COLLECTIONS', res.data)
        })
        .catch(err => console.error(err.response))
      },

      fetchCollectionsOrderBy({ commit, getters }, standard) {
        commit('SET_COLLECTIONS', [])
  
        let query = "?"
        query += `orderby=${standard}`

        axios({
          url: drf.collections.collection_list_orderby() + query,
          method:'get',
          headers: getters.authHeader, 
        })
        .then(res => {
          commit('SET_COLLECTIONS', res.data)
        })
        .catch(err => console.error(err.response))
      },

      fetchCollection({ commit, getters }, collectionPk) {
        commit('SET_COLLECTION', [])

        axios({
          url: drf.collections.collection_detail(collectionPk),
          method:'get',
          headers: getters.authHeader, 
        })
        .then(res => {
          commit('SET_COLLECTION', res.data)
        })
        .catch(err => console.error(err.response))
      },

      likeCollection({ commit, getters}, collectionPk) {
        axios({
          url: drf.collections.like_collection(collectionPk),
          method:'post',
          headers: getters.authHeader, 
        })
        .then((res) => {
          console.log(res.data)
          commit("SET_COLLECTION", res.data) 
        })
        .catch(err => console.error(err.response))
      },
      
      createCollection({ commit, getters }, collection) {
        axios({
          url: drf.collections.collection_list(),
          method:'post',
          data:collection,
          headers: getters.authHeader, 
        })
        .then(res => {
          console.log(res.data)
          commit('SET_COLLECTION', res.data)
          router.push({
            name: 'collection_detail',
            params: { collectionPk: getters.collection.pk }
          })
        })
      },

      updateCollection({ commit, getters }, { pk, title, description, movies}) {
        axios({
          url: drf.collections.collection_detail(pk),
          method:'put',
          data: { title, description, movies },
          headers: getters.authHeader, 
        })
        .then(res => {
          console.log(res.data)
          commit('SET_COLLECTION', res.data)
        })
      },
      searchCollections({ commit, getters }, keyword) {
        commit('SET_COLLECTIONS', [])

        let query = "?"
        if (keyword) {
          query += `keyword=${keyword}`
        }

        axios({
          url: drf.collections.collection_list()+query,
          method:'get',
          headers: getters.authHeader, 
        })
        .then(res => {
          console.log(res.data)
          commit('SET_COLLECTIONS', res.data)
        })
        .catch(err => console.error(err.response))
      },
      deleteCollection({ commit, getters}, pk) {
        axios({
          url: drf.collections.collection_detail(pk),
          method:'delete',
          headers: getters.authHeader, 
        })
        .then(res => {
          commit('SET_COLLECTIONS', res.data)
          router.push({
            name: 'collections',
          })
        })
        .catch(err => console.error(err.response))
      },
    }
  
  }
  
