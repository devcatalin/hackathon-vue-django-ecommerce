<template>
  <div class="m-t-lg m-l-lg m-r-lg">
    <b-button icon-left="arrow-left">Inapoi la site</b-button>
    <div class="product-detail m-t-lg">
      <img src="https://via.placeholder.com/400" alt />
      <div class="product-detail-panel">
        <h1>Title</h1>
        <h3 class="p-b-lg">128,58 lei</h3>
        <p
          class="m-b-xxl"
        >Lorem ipsum dolor, sit amet consectetur adipisicing elit. Recusandae aperiam porro laudantium, officiis veniam alias beatae deserunt, ut placeat fugiat libero voluptatibus. Ratione consequatur, eaque earum nostrum suscipit iure quis!</p>

        <b-field grouped class="v-align">
          <b-numberinput min="0" max="10" />
          <p class="control">
            <b-button size="is-large" type="is-primary">Cumpara acum</b-button>
          </p>
        </b-field>
      </div>
    </div>
    <h4 class="m-t-xl">Produse similare</h4>
    <hr />
    <div class="similar-products m-b-lg">
      <product-grid />
      <product-grid />
      <product-grid />
      <product-grid />
      <product-grid />
    </div>
  </div>
</template>

<script>
import ProductGrid from "../components/ProductGrid.vue";
export default {
  components: {
    ProductGrid
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
</style>
