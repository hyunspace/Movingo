<template>
  <div>
    <footer>
      <p>ⓒ 2022 All copyright reserved by
      <span><a href="mailto:jayl2cu@gmail.com">LEE JAEJUN</a></span>
      <span> & </span>
      <span><a href="mailto:at.hyunspace@gmail.com">KIM JIHYUN</a></span>
      </p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'InfoFooter'
}
</script>

<style scoped>
footer {
  display: flex;
  justify-content: center;
  margin: 5rem 0 2rem 0;
  color: #ffffff;
}
a {
  text-decoration: none;
  color: #ffffff;
}
a:hover {
  color: #e11616;
}
</style>