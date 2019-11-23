import http from '@/http';

export const productsModule = {
  state: {
    products: [],
    filteredProducts: [],
    filters: {
      category: "",
      subcategory: "",
      sellers: [],
      sort: ""
    }
  },
  getters: {
    products: state => state.products,
    filteredProducts: state => state.filteredProducts,
    filters: state => state.filters
  },
  mutations: {
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
    },
  },
  actions: {
    async fetchProducts({commit, getters}) {
      const { category, subcategory, sellers, sort } = getters.filters;
      commit('loading', true);
      const response = await http.post(`/api/shop/products/`, {
        category,
        subcategory,
        sellers,
        sort_option: sort
        // sellers: sellers.map(seller => {return {username: seller}})
      });
      commit('loading', false);
      commit('set_products', response.data);
    },
    async setFilters({commit, dispatch}, filters) {
      const { category, subcategory, sellers, sort } = filters;
      commit('loading', true);
      if (category || category === "") {
        commit('set_filters_category', category);
      }
      if (subcategory || subcategory === "") {
        commit('set_filters_subcategory', subcategory);
      }
      if (sellers || sellers === []) {
        commit('set_filters_sellers', sellers);
      }
      if (sort || sort === "") {
        commit('set_filters_sort', sort);
      }
      await dispatch('fetchProducts');
      commit('loading', false);
    }
  }
}
