import http from '@/http';

export const productsModule = {
  state: {
    products: [],
    filteredProducts: [],
    filters: {
      category: "",
      subcategory: "",
      sellers: []
    }
  },
  getters: {
    products: state => state.products,
    filteredProducts: state => state.filteredProducts
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
    },
    set_filters_subcategory(state, subcategory) {
      state.filters.subcategory = subcategory;
    },
    set_filters_sellers(state, sellers) {
      if (sellers.length === 0) {
        state.filters.sellers = undefined;
      } else {
        state.filters.sellers = sellers;
      }
    },
    apply_filters(state) {
      let filteredProducts = state.products;
      if (state.filters.category && state.filters.category !== "") {
        console.log("intra aici?");
        console.log(state.filters.category);
        console.log("cat-before", filteredProducts);
        filteredProducts = filteredProducts.filter(item => {
          return item.category.slug === state.filters.category;
        });
        console.log("cat-after", filteredProducts);
      }
      if (state.filters.subcategory && state.filters.subcategory !== "") {
        console.log("intra aici2?");
        console.log(state.filters.subcategory);
        console.log("sub-before", filteredProducts);
        filteredProducts = filteredProducts.filter(item => {
          return item.subcategory.slug === state.filters.subcategory;
        });
        console.log("sub-aftre", filteredProducts);
      }
      if (state.filters.sellers && state.filters.sellers.length > 0) {
        filteredProducts = filteredProducts.filter(item => {
          return state.filters.sellers.includes(item.seller);
        });
      }
      state.filteredProducts = filteredProducts;
    }
  },
  actions: {
    async fetchProducts({commit}, subcategory=null) {
      commit('loading', true);
      const response = await http.get(`/api/shop/products/`, {
        params: {
          subcategory
        }
      });
      commit('loading', false);
      commit('set_products', response.data);
      commit('set_filtered_products', response.data);
    },
    setProductFilters({commit}, payload) {
      const { category, subcategory, sellers } = payload;
      commit('loading', true);
      if (category) {
        commit('set_filters_category', category);
      }
      if (subcategory) {
        commit('set_filters_subcategory', subcategory);
      }
      if (sellers) {
        commit('set_filters_sellers', sellers)
      }
      commit('apply_filters');
      commit('loading', false);
    }
  }
}
