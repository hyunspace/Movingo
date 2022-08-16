import Vue from 'vue'
import Vuex from 'vuex'

import movies from './modules/movies'
import accounts from './modules/accounts'
import collections from './modules/collections'
import bingos from './modules/bingos'
import community from './modules/community'


Vue.use(Vuex)

export default new Vuex.Store({
  modules: { accounts, movies, collections, bingos, community }
})