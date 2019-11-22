import http from '@/http';

export const productsModule = {
  state: {
    products: []
  },
  getters: {

  },
  mutations: {
    set_products(state, products) {
      state.products = products;
    }
  },
  actions: {
    async getProducts({commit}, subcategory=null) {
      commit('loading', true);
      const response = await http.get(`/api/shop/products/`, {
        params: {
          subcategory
        }
      });
      commit('loading', false);
      commit('set_products', response.data);
    }
  }
}
