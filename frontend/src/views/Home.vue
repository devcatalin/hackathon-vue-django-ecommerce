<template>
  <div class="home-main p-t-lg p-l-sm">
    <span></span>
    <div class="sorting-panel m-b-sm">
      <span class="m-r-sm">Ordoneaza dupa:</span>
      <b-dropdown v-model="sortOption" aria-role="list" class="m-r-lg">
        <button class="button is-primary" type="button" slot="trigger">
          <template v-if="sortOption === 'Pret crescator'">
            <span>Pret crescator</span>
          </template>
          <template v-else-if="sortOption === 'Pret descrescator'">
            <span>Pret descrescator</span>
          </template>
          <template v-else>
            <span>Locatie</span>
          </template>
          <b-icon icon="menu-down"></b-icon>
        </button>

        <b-dropdown-item value="Pret crescator" aria-role="listitem">Pret crescator</b-dropdown-item>
        <b-dropdown-item value="Pret descrescator" aria-role="listitem">Pret descrescator</b-dropdown-item>
        <b-dropdown-item value="Locatie" aria-role="listitem">Locatie</b-dropdown-item>
      </b-dropdown>
      <span class="m-r-sm">Tip afisare:</span>
      <b-dropdown aria-role="list" v-model="viewOption">
        <button class="button is-primary" type="button" slot="trigger">
          <template v-if="viewOption === 'Grid'">
            <span>Grid</span>
          </template>
          <template v-else-if="viewOption === 'List'">
            <span>List</span>
          </template>
          <template v-else>
            <span>Harta</span>
          </template>
          <b-icon icon="menu-down"></b-icon>
        </button>

        <b-dropdown-item value="Grid" aria-role="listitem">Grid</b-dropdown-item>
        <b-dropdown-item value="List" aria-role="listitem">Lista</b-dropdown-item>
        <b-dropdown-item value="Harta" aria-role="listitem">Harta</b-dropdown-item>
      </b-dropdown>
    </div>

    <sidebar />
    <div>
      <product-grid v-if="viewOption == 'Grid'" title="Rosii" price="215,28" />
      <product-list v-else />
    </div>
  </div>
</template>

<script>
import Sidebar from "../components/Sidebar.vue";
import ProductGrid from "../components/ProductGrid.vue";
import ProductList from "../components/ProductList.vue";
export default {
  components: { Sidebar, ProductGrid, ProductList },
  data() {
    return {
      sortOption: "Pret crescator",
      viewOption: "Grid"
    };
  }
};
</script>

<style>
.home-main {
  background-color: #eeeeee;
  min-height: 100vh;
  display: grid;
  grid-template-columns: 15rem 1fr;
  grid-column-gap: 2rem;
  grid-row-gap: 0.8rem;
}

.highlight {
  color: blue;
}

.sorting-panel {
  display: flex;
  align-items: center;
}

i {
  cursor: pointer;
}
</style>
