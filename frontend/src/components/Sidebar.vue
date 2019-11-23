<template>
  <div class="card sidebar">
    <b-tabs :expanded="true" type="is-boxed">
      <b-tab-item label="Produse">
        <b-menu>
          <b-menu-list>
            <b-menu-item
              @click="clearCategoryFilter"
              :active="allProductsMenuItemActive"
              label="Toate produsele"
            ></b-menu-item>
          </b-menu-list>
          <b-menu-list v-for="category in categories" :key="category.title">
            <b-menu-item @click="setSelectedCategory(category.slug)" :label="category.title">
              <div v-for="subcategory in category.subcategories" :key="subcategory.title">
                <b-menu-item
                  @click="setSelectedSubcategory(subcategory.slug)"
                  :label="subcategory.title"
                ></b-menu-item>
              </div>
            </b-menu-item>
          </b-menu-list>
        </b-menu>
      </b-tab-item>

      <b-tab-item label="Producatori">
        <div class="field m-b-sm" style="border-bottom: 1px solid; padding-bottom: 10px;">
          <b-button class="m-l-lg" @click="clearSellersFilter">Toti producatorii</b-button>
        </div>
        <div v-for="seller in sellers" :key="seller.username" class="m-l-sm">
          <div class="field m-b-sm">
            <b-checkbox v-model="sellersFilter" :native-value="seller.username">{{seller.full_name}}</b-checkbox>
          </div>
        </div>
      </b-tab-item>
    </b-tabs>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      sellersFilter: [],
      selectedCategory: null,
      selectedSubcategory: null
    };
  },
  methods: {
    clearSellersFilter() {
      this.sellersFilter = [];
    },
    clearCategoryFilter() {
      this.selectedCategory = "";
    },
    setSelectedCategory(category) {
      this.selectedCategory = category;
    },
    setSelectedSubcategory(subcategory) {
      this.selectedSubcategory = subcategory;
    }
  },
  computed: {
    ...mapGetters(["categories", "sellers"]),
    allProductsMenuItemActive() {
      if (!this.selectedCategory || this.selectedCategory === "") {
        return true;
      }
      return false;
    }
  },
  watch: {
    sellersFilter() {
      this.$store.dispatch("setFilters", {
        sellers: this.sellersFilter
      });
    },
    selectedCategory() {
      this.$store.dispatch("setFilters", {
        category: this.selectedCategory
      });
    },
    selectedSubcategory() {
      this.$store.dispatch("setFilters", {
        subcategory: this.selectedSubcategory
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.sidebar {
  min-height: 100vh;
}
</style>
