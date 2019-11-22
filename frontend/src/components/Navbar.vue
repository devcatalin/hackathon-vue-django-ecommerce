<template>
  <b-navbar type="is-primary" spaced="true" shadow="true" fixed-top="true">
    <template slot="brand">
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        <span>LocalGoods</span>
      </b-navbar-item>
    </template>
    <template slot="end" v-if="!isAuthenticated">
      <router-link to="/login" exact v-slot="{ isActive, navigate }">
        <b-navbar-item @click="navigate" :active="isActive">Autentificare</b-navbar-item>
      </router-link>
      <router-link to="/register" exact v-slot="{ isActive, navigate }">
        <b-navbar-item @click="navigate" :active="isActive">Inregistrare</b-navbar-item>
      </router-link>
    </template>
  </b-navbar>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["isAuthenticated"])
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push("/login");
    }
  }
};
</script>

<style scoped>
.navbar-active {
  background-color: white;
  color: green;
}
</style>
