<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view></router-view>
    <info-footer></info-footer>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'
  import InfoFooter from '@/components/InfoFooter.vue'
  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar, InfoFooter },
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>

<style scoped>
  router-view{
    font-family: 'Pretendard';
  }
</style>
