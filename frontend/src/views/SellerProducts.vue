<template>
  <div class="seller-products m-xl">
    <user-profile />

    <b-button type="is-primary" class="m-b-lg" @click="showCreateModal">Adauga produs nou</b-button>

    <div>
      <b-table :bordered="true" :data="products">
        <template slot-scope="props">
          <b-table-column width="200" field="name" label="Nume produs">{{ props.row.title }}</b-table-column>
          <b-table-column field="description" label="Descriere">{{ props.row.description }}</b-table-column>
          <b-table-column
            width="150"
            field="category"
            label="Categorie"
          >{{ props.row.category.title }}</b-table-column>
          <b-table-column
            width="150"
            field="subcategory"
            label="Subcategorie"
          >{{ props.row.subcategory.title }}</b-table-column>
          <b-table-column width="80" field="u_m" label="U.M.">{{ props.row.quantity_type }}</b-table-column>
          <b-table-column field="cantity" label="Cantitate" width="100">{{ props.row.quantity }}</b-table-column>
          <b-table-column width="120" centered field="price" label="Pret">{{ props.row.price }}</b-table-column>
          <b-table-column width="50" field="price">
            <a @click="showDeleteModal(props.row.slug)">
              <b-icon type="is-danger" icon="delete"></b-icon>
            </a>
            <a @click="showUpdateModal(props.row.slug)">
              <b-icon type="is-info" icon="pencil"></b-icon>
            </a>
          </b-table-column>
        </template>
      </b-table>
    </div>

    <b-modal :active.sync="createModal.visible" has-modal-card :can-cancel="true">
      <product-create
        :closeModal="closeModal"
        :shouldUpdate="createModal.shouldUpdate"
        :product_slug="createModal.product_slug"
      />
    </b-modal>
    <b-modal :active.sync="deleteModal.visible" has-modal-card :can-cancel="true">
      <div class="card p-md modal-content">
        <h3 class="m-b-lg">Sunteti siguri ca doriti sa stergeti acest produs?</h3>
        <div class="flex-align">
          <b-button type="is-primary" @click="closeDeleteModal">Anuleaza</b-button>
          <b-button type="is-danger" @click.prevent="deleteProduct">Confirma</b-button>
        </div>
      </div>
    </b-modal>
  </div>
</template>

<script>
import ProductCreate from "../views/ProductCreate.vue";
import UserProfile from "../components/Profile.vue";
import http from "@/http";

export default {
  components: {
    UserProfile,
    ProductCreate
  },
  data() {
    return {
      deleteModal: {
        visible: false,
        product_slug: null
      },
      createModal: {
        visible: false,
        shouldUpdate: false,
        product_slug: null
      },
      products: []
    };
  },
  methods: {
    showCreateModal() {
      this.createModal = {
        visible: true,
        shouldUpdate: false,
        product_slug: null
      };
    },
    showUpdateModal(product_slug) {
      this.createModal = {
        visible: true,
        shouldUpdate: true,
        product_slug: product_slug
      };
    },
    showDeleteModal(product_slug) {
      this.deleteModal.visible = true;
      this.deleteModal.product_slug = product_slug;
    },
    closeDeleteModal() {
      this.deleteModal = {
        visible: false,
        product_slug: null
      };
    },
    closeModal() {
      this.createModal = {
        visible: false,
        shouldUpdate: false,
        product_slug: null
      };
      this.fetchSellerProducts();
    },
    fetchSellerProducts() {
      http.get("/api/shop/products/seller/").then(response => {
        this.products = response.data;
      });
    },
    async deleteProduct() {
      await this.$store.dispatch(
        "deleteProduct",
        this.deleteModal.product_slug
      );
      this.fetchSellerProducts();
      this.closeDeleteModal();
    }
  },
  beforeMount() {
    this.fetchSellerProducts();
  }
};
</script>

<style lang="scss" scoped>
.seller-products {
  min-height: 105vh;
}

h3 {
  font-size: 1.5rem;
}

.flex-align {
  display: flex;
  justify-content: space-between;
}

.flex-center {
  display: flex;
  justify-content: center;
}
</style>
