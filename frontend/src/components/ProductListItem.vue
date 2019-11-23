<template>
  <div class="card product-list-card m-b-md">
    <!-- <img :src="thumbnail" :alt="title" /> -->
    <div :style="`background-image: url(${product.thumbnail})`" class="thumbnail"></div>
    <div class="product-list-details">
      <h1>{{product.title}}</h1>
      <p>{{product.description}}</p>
      <p>Vândut de: {{product.seller}}</p>
      <div class="product-list-details-bottom">
        <span>{{product.price}} Lei</span>
        <router-link v-if="!isAuthenticated" to="/login" exact v-slot="{ navigate }">
          <b-button icon-left="cart" type="is-primary" @click="navigate">Adaugă în cos</b-button>
        </router-link>
        <b-button
          @click.prevent="addProductToCart"
          v-else
          icon-left="cart"
          type="is-primary"
        >Adaugă în cos</b-button>
      </div>
    </div>
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
  background-size: contain;
}
</style>
