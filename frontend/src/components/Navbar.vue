<template>
  <b-navbar type="is-primary" :spaced="true" :fixed-top="true">
    <template slot="brand">
      <b-navbar-item tag="router-link" :to="{ path: '/home' }">
        <p>LocalGoods</p>
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
    <template slot="end" v-if="isAuthenticated && !isSeller">
      <router-link to="/my-account" exact v-slot="{ isActive, navigate }">
        <b-navbar-item @click="navigate" :active="isActive">Contul meu</b-navbar-item>
      </router-link>
      <b-dropdown aria-role="menu" hoverable position="is-bottom-left">
        <b-button slot="trigger" type="is-primary" to="/shopping-cart" tag="router-link">
          <b-icon icon="cart" />
          <span
            style="font-weight: 700; background-color: black; border-radius: 50%; width: 25px; display:inline-block;"
          >{{cartItems.length}}</span>
          <b-icon icon="menu-down"></b-icon>
        </b-button>
        <b-dropdown-item custom aria-role="menuitem">
          <div class="shopping-cart-dropdown">
            <div>
              <router-link to="/shopping-cart">{{ cartItems.length }} produse in cos</router-link>
              <p>{{ cartTotal }} Lei</p>
            </div>
            <b-button
              to="/shopping-cart"
              size="is-small"
              class="is-primary"
              tag="router-link"
            >Trimite comanda</b-button>
          </div>
        </b-dropdown-item>
      </b-dropdown>
      <b-navbar-item @click="logout">Deconectare</b-navbar-item>
    </template>
    <template slot="end" v-if="isAuthenticated && isSeller">
      <router-link to="/seller-products" exact v-slot="{ isActive, navigate }">
        <b-navbar-item @click="navigate">Contul meu</b-navbar-item>
      </router-link>
      <b-navbar-item @click="logout">Deconectare</b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["isAuthenticated", "cartItems", "isSeller", "cartTotal"])
  },
  methods: {
    logout() {
      this.$buefy.dialog.confirm({
        message: "Esti sigur ca vrei sa te deconectezi?",
        onConfirm: () => {
          this.$store.dispatch("logout");
          this.$router.push("/login");
          this.$buefy.toast.open("Te-ai deconectat cu succes.");
        }
      });
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

.z-index {
  z-index: 10000;
}
</style>
