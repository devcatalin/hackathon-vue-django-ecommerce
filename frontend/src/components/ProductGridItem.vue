<template>
  <div class="card product-grid-card">
    <figure class="image is-4by3">
      <img :src="product.thumbnail" :alt="product.title" />
    </figure>
    <div class="card-content">
      <router-link :to="`/products/detail/${product.slug}`" exact>
        <h2 class="m-b-sm">{{ product.title }}</h2>
      </router-link>
      <p>{{ product.price }} Lei / {{ product.quantity_type }}</p>
      <p>Vândut de: {{ product.seller }}</p>
      <p>Stoc: {{ product.quantity }} - {{ product.quantity_type }}</p>
    </div>
    <router-link to="/login" v-if="!isAuthenticated">
      <b-icon class="m-r-sm" icon="cart" size="is-small"></b-icon>Adaugă
      în coș
    </router-link>
    <a
      v-else-if="product.quantity === 0"
      style="background-color: grey; cursor: default;"
      class="buton-a"
    >
      <b-icon class="m-r-sm" icon="cart" size="is-small"></b-icon>Stoc epuizat
    </a>
    <a @click.prevent="addProductToCart" v-else class="buton-a">
      <b-icon class="m-r-sm" icon="cart" size="is-small"></b-icon>Adaugă
      în coș
    </a>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  props: ["product"],
  computed: {
    ...mapGetters(["isAuthenticated"])
  },
  methods: {
    addProductToCart() {
      this.$store.dispatch("addCartItem", this.product);
    }
  }
};
</script>

<style lang="scss" scoped>
.product-grid-card {
  height: 22rem;
  width: 16rem;

  display: grid;
  grid-template-rows: max-content 1fr 2rem;
  align-items: center;
}

h2 {
  font-size: 1.5rem;
  font-weight: 500;
  text-align: center;
  margin-bottom: 1rem;
}

p {
  text-align: center;
}

.buton-a {
  text-align: center;
  background-color: #2e7d32;
  color: white;
  padding: 0.5rem;
  transition: all 0.5s;
}

.buton-a:hover {
  background-color: #4caf50;
}
</style>
