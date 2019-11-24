import http from "@/http";

export const productsModule = {
  state: {
    products: [],
    filteredProducts: [],
    filters: {
      category: "",
      subcategory: "",
      sellers: [],
      sort: ""
    },
    sellers: []
  },
  getters: {
    sellers: state => state.sellers,
    products: state => state.products,
    filteredProducts: state => state.filteredProducts,
    filters: state => state.filters
  },
  mutations: {
    set_sellers(state, sellers) {
      state.sellers = sellers;
    },
    set_products(state, products) {
      state.products = products;
    },
    set_filtered_products(state, filtered) {
      state.filteredProducts = filtered;
    },
    set_filters_category(state, category) {
      state.filters.category = category;
      state.filters.subcategory = "";
    },
    set_filters_subcategory(state, subcategory) {
      state.filters.subcategory = subcategory;
    },
    set_filters_sort(state, sort) {
      state.filters.sort = sort;
    },
    set_filters_sellers(state, sellers) {
      if (sellers.length === 0) {
        state.filters.sellers = [];
      } else {
        state.filters.sellers = sellers;
      }
    }
  },
  actions: {
    async fetchProducts({ commit, getters }) {
      const { category, subcategory, sellers, sort } = getters.filters;
      commit("loading", true);
      const response = await http.post(`/api/shop/products/`, {
        category,
        subcategory,
        sellers,
        sort_option: sort
        // sellers: sellers.map(seller => {return {username: seller}})
      });
      commit("loading", false);
      commit("set_products", response.data.products);
      commit("set_sellers", response.data.sellers);
    },
    async setFilters({ commit, dispatch }, filters) {
      const { category, subcategory, sellers, sort } = filters;
      commit("loading", true);
      if (category || category === "") {
        commit("set_filters_category", category);
      }
      if (subcategory || subcategory === "") {
        commit("set_filters_subcategory", subcategory);
      }
      if (sellers || sellers === []) {
        commit("set_filters_sellers", sellers);
      }
      if (sort || sort === "") {
        commit("set_filters_sort", sort);
      }
      await dispatch("fetchProducts");
      commit("loading", false);
    },
    async createProduct({ commit, dispatch }, payload) {
      commit("loading", true);
      var formData = new FormData();
      formData.append("thumbnail", payload.thumbnail);
      formData.append("title", payload.title);
      formData.append("description", payload.description);
      formData.append("price", payload.price);
      formData.append("quantity_type", payload.quantity_type);
      formData.append("quantity", payload.quantity);
      formData.append("subcategory", payload.subcategory);
      await http.post("/api/shop/products/create/", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });
      dispatch("fetchProducts");
      commit("loading", false);
    },
    async updateProduct({ commit, dispatch }, payload) {
      commit("loading", true);
      var formData = new FormData();
      formData.append("product_slug", payload.product_slug);
      if (payload.thumbnail) {
        formData.append("thumbnail", payload.thumbnail);
      }
      formData.append("title", payload.title);
      formData.append("description", payload.description);
      formData.append("price", payload.price);
      formData.append("quantity_type", payload.quantity_type);
      formData.append("quantity", payload.quantity);
      formData.append("subcategory", payload.subcategory);
      await http.post("/api/shop/products/update/", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });
      dispatch("fetchProducts");
      commit("loading", false);
    },
    async deleteProduct({ commit, dispatch }, product_slug) {
      commit("loading", true);
      await http.post("/api/shop/products/delete/", {
        product_slug
      });
      dispatch("fetchProducts");
      commit("loading", false);
    }
  }
};
