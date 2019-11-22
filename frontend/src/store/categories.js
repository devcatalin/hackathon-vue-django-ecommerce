import http from '@/http';

export const categoriesModule = {
  state: {
    categories: []
  },
  getters: {

  },
  mutations: {
    set_categories(state, categories) {
      state.categories = categories;
    }
  },
  actions: {
    async get_categories({commit}) {
      commit('loading', true);
      const response = await http.get('/api/shop/categories/');
      commit('loading', false);
      commit('set_categories', response.data);
    }
  }
}
