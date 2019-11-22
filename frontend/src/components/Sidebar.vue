<template>
  <div class="card sidebar">
    <b-tabs expanded="true" type="is-boxed">
      <b-tab-item label="Produse">
        <b-menu>
          <b-menu-list v-for="category in categories" :key="category">
            <b-menu-item :label="category.name">
              <div v-for="subcategory in category.subcategories" :key="subcategory">
                <b-menu-item :label="subcategory"></b-menu-item>
              </div>
            </b-menu-item>
          </b-menu-list>
        </b-menu>
      </b-tab-item>

      <b-tab-item label="Producatori">
        <div v-for="manufacturer in manufacturers" :key="manufacturer" class="m-l-sm">
          <div class="field m-b-sm">
            <b-checkbox v-model="manufacturersFilter" :native-value="manufacturer">{{manufacturer}}</b-checkbox>
          </div>
        </div>
      </b-tab-item>
    </b-tabs>
  </div>
</template>

<script>
export default {
  data() {
    return {
      categories: [
        { name: "Legume", subcategories: ["Rosii", "Castraveti", "Cartofi"] },
        { name: "Lactate", subcategories: ["Lapte", "Oua", "Unt", "Iaurt"] },
        { name: "Carne", subcategories: ["Sunca", "Salam"] }
      ],
      manufacturers: ["Agil", "Sim", "Cris Tim"],
      manufacturersFilter: []
    };
  }
};
</script>

<style lang="scss" scoped>
.sidebar {
  min-height: 100vh;
}
</style>