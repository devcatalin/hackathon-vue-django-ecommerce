<template>
  <div class="m-t-lg m-l-lg m-r-lg">
    <router-link to="/products" exact v-slot="{ navigate }">
      <b-button @click="navigate" icon-left="arrow-left">Înapoi la toate produsele</b-button>
    </router-link>
    <div class="product-detail m-t-lg">
      <img :src="product.thumbnail" alt />
      <div class="product-detail-panel">
        <h1>{{product.title}}</h1>
        <h3 class="p-b-lg">{{product.price}} lei</h3>
        <p class="m-b-xxl">{{product.description}}</p>
      </div>
      <h4 class="m-t-xl">Produse similare</h4>
      <hr />
      <div class="similar-products m-b-lg">
        <product-grid
          v-for="sim_prod in similar_products"
          :key="sim_prod.slug"
          :product="sim_prod"
        />
      </div>
    </div>
  </div>
</template>

<script>
import http from "@/http";
import ProductGrid from "../components/ProductGridItem.vue";
export default {
  data() {
    return {
      product: null,
      similar_products: []
    };
  },
  components: {
    ProductGrid
  },
  beforeMount() {
    http
      .post("/api/shop/products/detail/", {
        product_slug: this.$route.params.slug
      })
      .then(response => {
        this.product = response.data.product;
        this.similar_products = response.data.similar_products;
      })
      .catch(() => {
        this.$router.push("/products");
      });
  },
  methods: {
    addProductToCart() {
      this.$store.dispatch("addCartItem", this.product);
    }
  }
};
</script>

<style scoped lang="scss">
.product-detail {
  display: grid;
  grid-template-columns: max-content 1fr;
  column-gap: 5rem;

  &-panel {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
}

img {
  width: 50rem;
  height: 35rem;
}

h1 {
  font-size: 2.5rem;
  font-weight: 500;
}

h3 {
  font-size: 1.5rem;
}

h4 {
  font-size: 1.5rem;
}

.similar-products {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  grid-row-gap: 2rem;
  grid-column-gap: 1rem;
}

.v-align {
  display: flex;
  align-items: center;
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
