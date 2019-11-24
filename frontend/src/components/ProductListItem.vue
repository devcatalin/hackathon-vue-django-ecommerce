<template>
  <div class="card product-list-card m-b-md">
    <!-- <img :src="thumbnail" :alt="title" /> -->
    <div :style="`background-image: url(${product.thumbnail})`" class="thumbnail"></div>
    <div class="product-list-details">
      <router-link :to="`/products/detail/${product.slug}`" exact>
        <h1>{{ product.title }}</h1>
      </router-link>
      <p>{{ product.description }}</p>
      <p>Vândut de: {{ product.seller }}</p>
      <p>Stoc: {{ product.quantity }} - {{ product.quantity_type }}</p>
      <div class="product-list-details-bottom">
        <span>{{ product.price }} Lei / {{ product.quantity_type }}</span>
        <div v-if="user.profile.user_type !== 'seller'">
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
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  props: ["product"],
  computed: {
    ...mapGetters(["isAuthenticated", "user"])
  },
  methods: {
    addProductToCart() {
      this.$store.dispatch("addCartItem", this.product);
    }
  }
};
</script>

<style lang="scss" scoped>
.product-list-card {
  width: 95%;
  height: 12rem;

  display: grid;
  grid-template-columns: 12rem 1fr;
  grid-column-gap: 1rem;
  grid-template-rows: 12rem;
}

.product-list-details {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  padding: 0.7rem;

  &-bottom {
    display: flex;
    justify-content: space-between;
  }
}

h1,
p {
  text-align: center;
}

span {
  font-size: 1.3rem;
}

h1 {
  font-size: 1.8rem;
}

.thumbnail {
  background-position: center;
  background-size: cover;
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
