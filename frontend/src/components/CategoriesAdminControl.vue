<template>
  <div class="categories p-l-xxl p-r-xxl m-b-lg">
    <div class="admin-category">
      <h1 class="m-b-md">Categorii</h1>
      <hr />
      <div class="cat-subcat-display m-b-md" v-for="category in categories" :key="category.slug">
        <button class="button" @click="setSelectedCategory(category)">{{ category.title }}</button>
        <a @click="categoryDelete(category)">
          <b-icon type="is-danger" class="m-l-md" icon="close"></b-icon>
        </a>
      </div>
      <div class="flex-center">
        <a v-if="!showCategoryInput" @click="displayCategoryInput">Adaugati categorie noua</a>
        <b-field label="Nume categorie" v-else>
          <b-input
            icon="plus"
            :icon-clickable="true"
            v-model="categoryInput"
            @icon-click="createCategory"
            @keyup.native.enter="createCategory"
          />
        </b-field>
      </div>
    </div>
    <div class="admin-subcategory">
      <h1 class="m-b-md">Subcategorii</h1>
      <hr />
      <div v-if="selectedCategory">
        <div
          class="cat-subcat-display m-b-md"
          v-for="subcategory in selectedCategory.subcategories"
          :key="subcategory.slug"
        >
          <b-button>{{ subcategory.title }}</b-button>
          <a @click="subcategoryDelete(subcategory)">
            <b-icon type="is-danger" class="m-l-md" icon="close"></b-icon>
          </a>
        </div>
        <div class="flex-center">
          <a
            v-if="!showSubcategoryInput"
            @click="displaySubcategoryInput"
          >Adaugati subcategorie noua</a>

          <b-field v-else label="Nume subcategorie">
            <b-input
              icon="plus"
              :icon-clickable="true"
              v-model="subcategoryInput"
              @icon-click="createSubcategory"
              @keyup.native.enter="createSubcategory"
            />
          </b-field>
        </div>
      </div>
    </div>

    <!-- <b-modal :active.sync="categoryDelete" has-modal-card :can-cancel="true">
      <div class="card p-md modal-content">
        <h3 class="m-b-lg">Sunteti siguri ca doriti sa stergeti aceasta categorie?</h3>
        <div class="flex-align">
          <b-button type="is-primary" @click="setCategoryDelete">Anuleaza</b-button>
          <b-button type="is-danger">Confirma</b-button>
        </div>
      </div>
    </b-modal>
    <b-modal :active.sync="subcategoryDelete" has-modal-card :can-cancel="true">
      <div class="card p-md modal-content">
        <h3 class="m-b-lg">Sunteti siguri ca doriti sa stergeti aceasta subcategorie?</h3>
        <div class="flex-align">
          <b-button type="is-primary" @click="setSubcategoryDelete">Anuleaza</b-button>
          <b-button type="is-danger">Confirma</b-button>
        </div>
      </div>
    </b-modal>-->
  </div>
</template>

<script>
import http from "@/http";
import { mapGetters } from "vuex";
export default {
  computed: {
    ...mapGetters(["categories"])
  },
  data() {
    return {
      //   categoryDelete: false,
      //   subcategoryDelete: false,
      selectedCategory: null,
      showCategoryInput: false,
      showSubcategoryInput: false,
      categoryInput: "",
      subcategoryInput: ""
    };
  },
  methods: {
    setSelectedCategory(category) {
      this.selectedCategory = category;
    },
    displayCategoryInput() {
      this.showCategoryInput = true;
    },
    hideCategoryInput() {
      this.showCategoryInput = false;
    },
    createCategory() {
      if (this.categoryInput == "") {
        return;
      }
      http
        .post("/api/shop/categories/create/", {
          title: this.categoryInput
        })
        .then(() => {
          this.$store.dispatch("fetchCategories");
          this.$buefy.toast.open("Categoria a fost adaugata!");
          this.hideCategoryInput();
        });
    },
    displaySubcategoryInput() {
      this.showSubcategoryInput = true;
    },
    hideSubcategoryInput() {
      this.showSubcategoryInput = false;
    },
    createSubcategory() {
      if (this.subcategoryInput == "") {
        return;
      }
      http
        .post("/api/shop/subcategories/create/", {
          title: this.subcategoryInput,
          category_slug: this.selectedCategory.slug
        })
        .then(() => {
          this.$store.dispatch("fetchCategories");
          this.$buefy.toast.open("Subcategoria a fost adaugata!");
          this.selectedCategory = "";
          this.hideSubcategoryInput();
        });
    },
    categoryDelete(categ) {
      http
        .post("/api/shop/categories/delete/", {
          category_slug: categ.slug
        })
        .then(() => {
          this.$store.dispatch("fetchCategories");
          this.$buefy.toast.open("Categoria a fost stearsa.");
          this.selectedCategory = "";
        });
    },
    subcategoryDelete(subcateg) {
      http
        .post("/api/shop/subcategories/delete/", {
          subcategory_slug: subcateg.slug
        })
        .then(() => {
          this.$store.dispatch("fetchCategories");
          this.$buefy.toast.open("Subcategoria a fost stearsa.");
          this.selectedCategory = "";
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.categories {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 3rem;
}
.cat-subcat-display {
  display: grid;
  grid-template-columns: repeat(2, min-content);
  justify-content: center;
  align-items: center;
}
h1 {
  font-size: 1.4rem;
  text-align: center;
}

a {
  text-align: center;
}

h3 {
  font-size: 1.3rem;
}
</style>
