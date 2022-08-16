<template>
  <div id="suggestions"> 
    <div v-for="suggest in suggests" :key="suggest.title">
      <div @click="select_suggestion(suggest.title)" class="suggestion-item">{{ suggest.title }}</div>
    </div>
  </div>  
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: "AutoCompleteSuggestions",
  computed: {
    ...mapGetters(['suggests']),
  },
  methods: {
    ...mapActions(['deleteSuggestion']),
    select_suggestion(title) {
      this.$emit('titleFromSuggestions', title)
      this.deleteSuggestion()
    },
    summary(a) {
      return a.splice(0, 20)
    }
    // filter(title) {
    //   return title.length > 10 ? title.splice(0, 10)+"..." : title
    // }
  },
}
</script>

<style scoped>
#suggestions {
  border-top: 0.5px solid;
  background:black;
}
.suggestion-item {
  padding: 5px;
  width:250px;
  background: black;
  border-top: 1px solid #888;
  cursor: pointer;
  overflow: hidden;
}
.suggestion-item:hover {
  color:black;
  background: #eee;
}
</style>