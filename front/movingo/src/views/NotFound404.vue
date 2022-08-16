<template>
  <div>
    <!-- <img class="not-found" src="@/assets/404.jpg" alt="not-found"> -->
    <div class="d-flex flex-column align-items-center">
      <p><img class="not-found-img" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F435K8%2FbtrC3DM60IL%2F6bIEFWqPhYTL7Y8KRxUvkK%2Fimg.jpg" alt="404 not found"></p>
      <h5 class="not-found-text">앗, 길을 잘못 들었어요!</h5>
      <button class="go-back-btn" @click="goBack">뒤로 돌아가기</button>
      <p><a class="img-source" href="https://www.freepik.com/vectors/server-error">Server error vector created by storyset</a></p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'NotFound404',
    methods: {
      goBack() {
        this.$router.go(-1); [2]
      }
    }
  }
</script>

<style scoped>
  p {
    text-align: center;
  }
  .not-found-img {
    width: 50%;
    margin-top: 50px;
  }
  .not-found-text {
    color: #ffffff;
    text-align: center;
    margin-top: 40px;
  }
  .img-source {
    color: #40444b;
    display: flex;
    justify-content: center;
    text-decoration: none;
  }
  .go-back-btn {
    width: 13rem;
    height: 3rem;
    background-color: #40444b;
    border: transparent;
    border-radius: 6px;
    color: #ffffff;
    font-size: 1.5rem;
    font-weight: bold;
    margin: 10px 0px 40px 0px;
  }
</style>
