import axios from 'axios';

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
      const response = await axios.get('/api/shop/categories/');
      commit('loading', false);
      commit('set_categories', response.data);
    }
  }
}
