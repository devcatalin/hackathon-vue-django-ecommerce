<template>
  <div class="card sidebar">
    <b-tabs :expanded="true" type="is-boxed">
      <b-tab-item label="Produse">
        <b-menu>
          <b-menu-list v-for="category in categories" :key="category.title">
            <b-menu-item :label="category.title">
              <div v-for="subcategory in category.subcategories" :key="subcategory.title">
                <b-menu-item :label="subcategory.title"></b-menu-item>
              </div>
            </b-menu-item>
          </b-menu-list>
        </b-menu>
      </b-tab-item>

      <b-tab-item label="Producatori">
        <div class="field m-b-sm" style="border-bottom: 1px solid; padding-bottom: 10px;">
          <small-button text="Toti producatorii" @click="clearSellersFilter">Toti producatorii</small-button>
        </div>
        <div v-for="seller in sellers" :key="seller.full_name" class="m-l-sm">
          <div class="field m-b-sm">
            <b-checkbox
              v-model="sellersFilter"
              :native-value="seller.full_name"
            >{{seller.full_name}}</b-checkbox>
          </div>
        </div>
      </b-tab-item>
    </b-tabs>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import SmallButton from "../components/SmallButton.vue";

export default {
  components: {
    SmallButton
  },
  data() {
    return {
      sellersFilter: []
    };
  },
  methods: {
    clearSellersFilter() {
      this.sellersFilter = [];
    }
  },
  computed: {
    ...mapGetters(["categories", "sellers"])
  }
};
</script>

<style lang="scss" scoped>
.sidebar {
  min-height: 100vh;
}
</style>
