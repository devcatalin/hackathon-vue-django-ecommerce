<template>
  <div class="product-create">
    <form v-on:submit.prevent="createProduct" class="card p-lg">
      <b-field label="Titlu">
        <b-input type="text" v-model="title" />
      </b-field>
      <b-field>
        <b-upload v-model="thumbnail">
          <a class="button is-primary">
            <b-icon icon="upload"></b-icon>
            <span>Adăugare poză</span>
          </a>
        </b-upload>
        <span class="file-name" v-if="thumbnail">{{ thumbnail.name }}</span>
      </b-field>
      <b-field label="Descriere">
        <b-input type="textarea" v-model="description" />
      </b-field>
      <div class="flex-align">
        <b-field>
          <b-select placeholder="Selectați o categorie" v-model="selectedCategory">
            <option
              v-for="category in categories"
              :key="category.slug"
              :value="category"
            >{{ category.title }}</option>
          </b-select>
        </b-field>
        <b-field>
          <b-select placeholder="Selectați o subcategorie" v-model="selectedSubcategory">
            <option
              v-for="subcategory in subcategories"
              :key="subcategory.slug"
              :value="subcategory"
            >{{ subcategory.title }}</option>
          </b-select>
        </b-field>
      </div>

      <b-field label="Unitate de măsura">
        <div class="block">
          <b-radio v-model="quantity_type" name="quantityType" native-value="kg">Kilogram</b-radio>
          <b-radio v-model="quantity_type" name="quantityType" native-value="buc">Bucată</b-radio>
        </div>
      </b-field>
      <div class="flex-align">
        <b-field label="Cantitate">
          <b-input min="0" type="float" v-model="quantity" />
        </b-field>
        <b-field label="Preț pe unitate">
          <b-input type="float" v-model="price" />
        </b-field>
      </div>

      <button class="button is-primary" type="submit">Salveaza</button>
    </form>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      selectedCategory: "",
      selectedSubcategory: "",
      subcategories: [],
      title: "",
      price: "",
      description: "",
      thumbnail: null,
      quantity_type: "kg",
      quantity: 0
    };
  },
  props: ["closeModal", "shouldUpdate", "product_slug"],
  computed: {
    ...mapGetters(["categories"])
  },
  mounted() {
    this.selectedCategory = this.categories[0];
  },
  watch: {
    selectedCategory() {
      this.subcategories = this.selectedCategory.subcategories;
      this.selectedSubcategory = this.selectedCategory.subcategories[0];
    }
  },
  methods: {
    async createProduct() {
      if (!this.shouldUpdate) {
        await this.$store.dispatch("createProduct", {
          title: this.title,
          price: this.price,
          description: this.description,
          quantity_type: this.quantity_type,
          quantity: this.quantity,
          subcategory: this.selectedSubcategory.slug,
          thumbnail: this.thumbnail
        });
      } else {
        await this.$store.dispatch("updateProduct", {
          product_slug: this.product_slug,
          title: this.title,
          price: this.price,
          description: this.description,
          quantity_type: this.quantity_type,
          quantity: this.quantity,
          subcategory: this.selectedSubcategory.slug,
          thumbnail: this.thumbnail
        });
      }
      this.closeModal();
    }
  }
};
</script>

<style lang="scss" scoped>
.product-create {
  display: grid;
  grid-template-rows: repeat(2, min-content);
  grid-gap: 3rem;
  justify-items: center;
  align-content: center;

  height: 96vh;
}

form {
  display: grid;
  grid-template-columns: 25rem;
  grid-gap: 1rem;
}
</style>
