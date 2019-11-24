<template>
  <div class="m-t-md p-lg">
    <b-table :data="products">
      <template slot-scope="props">
        <b-table-column field="name" label="Nume produs">
          {{
          props.row.title
          }}
        </b-table-column>
        <b-table-column field="category" label="Categorie">
          {{
          props.row.category.title
          }}
        </b-table-column>
        <b-table-column field="quantity_type" label="U.M.">
          {{
          props.row.quantity_type
          }}
        </b-table-column>
        <b-table-column field="quantity" label="Cantitate">
          {{
          props.row.quantity
          }}
        </b-table-column>
        <b-table-column field="price" label="Pret pe unitate">{{ props.row.price }} Lei</b-table-column>
        <b-table-column field="seller" label="Vânzător">
          {{
          props.row.seller
          }}
        </b-table-column>
        <b-table-column width="50">
          <a @click="deleteProduct(props.row.slug)">
            <b-icon type="is-danger" icon="delete"></b-icon>
          </a>
        </b-table-column>
      </template>
    </b-table>

    <h2 class="m-t-xl level-right">Număr de anunțuri: {{ products.length }}</h2>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import http from "@/http";

export default {
  computed: {
    ...mapGetters(["products"])
  },
  beforeMount() {
    this.$store.dispatch("fetchProducts");
  },
  methods: {
    deleteProduct(product_slug) {
      http
        .post("/api/shop/products/delete/", {
          product_slug: product_slug
        })
        .then(() => {
          this.$store.dispatch("fetchProducts");
          this.$buefy.toast.open("Produsul a fost sters cu succes.");
        });
    }
  }
};
</script>

<style lang="scss" scoped>
h2 {
  font-size: 1.5rem;
  font-weight: 600;
}

h3 {
  font-size: 1.3rem;
}
</style>
