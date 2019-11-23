import http from '@/http';

export const categoriesModule = {
  state: {
    categories: []
  },
  getters: {
    categories: state => state.categories
  },
  mutations: {
    setCategories(state, categories) {
      state.categories = categories;
    }
  },
  actions: {
    async fetchCategories({commit}) {
      commit('loading', true);
      const response = await http.get('/api/shop/categories/');
      commit('loading', false);
      commit('setCategories', response.data);
    }
  }
}
