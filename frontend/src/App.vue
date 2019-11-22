<template>
  <div id="app">
    <b-loading :is-full-page="true" :active.sync="isLoading"></b-loading>
    <Sidebar></Sidebar>
    <div class="app-grid">
      <div></div>
      <div class="app-right">
        <router-view />
        <Footer></Footer>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "./components/Sidebar.vue";
import { mapGetters } from "vuex";

export default {
  components: { Sidebar },
  computed: {
    ...mapGetters(["isLoading"])
  }
};
</script>

<style lang="scss">
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: inherit;
}

html {
  box-sizing: border-box;
  font-size: 62.5%; /* 1rem = 10px */
}

a {
  text-decoration: none;
}

.app-grid {
  display: grid;
  grid-template-columns: 16% 1fr;
  min-height: 100vh;
}

.app-right {
  background-color: #f6f6f6;
}

@media only screen and (max-width: 950px) {
  html {
    font-size: 85% !important;
  }
}
@media only screen and (min-width: 1700px) {
  html {
    font-size: 125% !important;
  }
}

@media only screen and (max-width: 1150px) {
  .app-grid {
    grid-template-columns: 0rem 1fr;
  }
}
</style>
