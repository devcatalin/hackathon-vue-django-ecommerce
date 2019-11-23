import http from '@/http';

export const productsModule = {
  state: {
    products: [],
    filteredProducts: []
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
    },
    productsFilter({commit, getters}, payload) {
      let { category, subcategory, sellers } = payload;
      sellers = ["vanzator"]
      let products = getters.products;
      if (category) {
        products = products.filter(item => {
          return item.subcategory.category.slug == category;
        });
      }
      if (subcategory) {
        products = products.filter(item => {
          return item.subcategory.slug == subcategory;
        });
      }
      if (sellers) {
        products = products.filter(item => {
          return sellers.includes(item.seller);
        });
      }
      commit('set_filtered_products', products)
    }
  }
}
