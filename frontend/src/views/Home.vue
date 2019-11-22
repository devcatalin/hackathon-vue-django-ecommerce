<template>
  <div class="home-main p-t-lg p-l-sm">
    <span></span>
    <div>
      <b-dropdown aria-role="list" class="m-b-lg">
        <button class="button is-primary" slot="trigger">
          <span>Ordoneaza dupa</span>
          <b-icon icon="menu-down"></b-icon>
        </button>

        <b-dropdown-item aria-role="listitem">Pret crescator</b-dropdown-item>
        <b-dropdown-item aria-role="listitem">Pret descrescator</b-dropdown-item>
        <b-dropdown-item aria-role="listitem">Locatie</b-dropdown-item>
      </b-dropdown>
      <b-dropdown aria-role="list" class="m-b-lg">
        <button class="button is-primary" slot="trigger">
          <span>Vizualizare</span>
          <b-icon icon="menu-down"></b-icon>
        </button>

        <b-dropdown-item aria-role="listitem">Grid</b-dropdown-item>
        <b-dropdown-item aria-role="listitem">Lista</b-dropdown-item>
        <b-dropdown-item aria-role="listitem">Harta</b-dropdown-item>
      </b-dropdown>
    </div>

    <sidebar />
    <div>
      <product-grid title="Rosii" price="215,28" />
    </div>
  </div>
</template>

<script>
import Sidebar from "../components/Sidebar.vue";
import ProductGrid from "../components/ProductList.vue";
export default {
  components: { Sidebar, ProductGrid }
};
</script>

<style>
.home-main {
  background-color: #eeeeee;
  min-height: 100vh;
  display: grid;
  grid-template-columns: 15rem 1fr;
  grid-column-gap: 2rem;
}
</style>
