import http from "@/http";


export const sellersModule = {
  state: {
    sellers: []
  },
  getters: {
    sellers: state => state.sellers
  },
  mutations: {
    setSellers(state, sellers) {
      state.sellers = sellers;
    }
  },
  actions: {
    async fetchSellers({commit}) {
      commit('loading', true);
      const response = await http.get('/api/users/sellers/');
      commit('loading', false);
      commit('setSellers', response.data);
    }
  }
}
