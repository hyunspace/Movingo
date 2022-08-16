<template>
  <div id="community-view">
    <h2>커뮤니티</h2>
    <p>영화에 대해 이야기를 나누어 보세요</p>
    <div v-for="thread in threads" :key="thread.pk">
      <community-poster class="community-item" :thread="thread"></community-poster>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import CommunityPoster from '@/components/community/CommunityPoster'

export default {
  name: "CommunityView",
  components: {
    CommunityPoster
  },
  computed: {
    ...mapGetters(['threads'])
  },
  methods:{
    ...mapActions(['fetchThreads'])
  },
  created() {
    this.fetchThreads()
  },
}
</script>

<style scoped>
#community-view{
  color:white;
  padding:20px;
}
</style>