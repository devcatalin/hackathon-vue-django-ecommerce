<template>
  <b-navbar type="is-primary" :spaced="true" :shadow="true" :fixed-top="true">
    <template slot="brand">
      <b-navbar-item tag="router-link" :to="{ path: '/home' }">
        <p>LocalGoods</p>
      </b-navbar-item>
    </template>
    <template slot="end" v-if="isAuthenticated">
      <router-link to="/login" exact v-slot="{ isActive, navigate }">
        <b-navbar-item @click="navigate" :active="isActive">Autentificare</b-navbar-item>
      </router-link>
      <router-link to="/register" exact v-slot="{ isActive, navigate }">
        <b-navbar-item @click="navigate" :active="isActive">Inregistrare</b-navbar-item>
      </router-link>
    </template>
    <template slot="end" v-else>
      <b-dropdown aria-role="menu" hoverable position="is-bottom-left" v-if="isSeller">
        <b-button slot="trigger" type="is-primary" to="/shopping-cart" tag="router-link">
          <b-icon icon="cart"></b-icon>
          <span>Cos de cumparaturi</span>
          <b-icon icon="menu-down"></b-icon>
        </b-button>
        <b-dropdown-item custom aria-role="menuitem">
          <div class="shopping-cart-dropdown">
            <div>
              <router-link to="/shopping-cart">x produse in cos</router-link>
              <p>5,823 Lei</p>
            </div>
            <b-button size="is-small" class="is-primary">Trimite comanda</b-button>
          </div>
        </b-dropdown-item>
      </b-dropdown>
      <router-link to="/seller-products" exact v-slot="{ isActive, navigate }" v-else>
        <b-navbar-item @click="navigate">Lista produse</b-navbar-item>
      </router-link>
      <router-link to="/home" exact v-slot="{ isActive, navigate }">
        <b-navbar-item @click="navigate">Deconectare</b-navbar-item>
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
.shopping-cart-dropdown {
  display: grid;
  grid-template-columns: repeat(2, max-content);
  grid-gap: 1rem;
  align-items: center;
}

p {
  font-weight: 700;
  font-size: 1.1rem;
}

p {
  font-family: "Boogaloo", cursive;
  font-size: 1.8rem;
}
</style>
