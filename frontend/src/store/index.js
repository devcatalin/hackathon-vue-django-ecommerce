import Vue from "vue";
import Vuex from "vuex";

import { authModule } from './auth';
import { categoriesModule } from './categories';
import { productsModule } from './products';
import { sellersModule } from './sellers';
import { shoppingCartModule } from './shoppingCart';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loading: false,
  },
  getters: {
    isLoading: state => !!state.loading,
  },
  mutations: {
    loading(state, value) {
      state.loading = value;
    }
  },
  modules: {
    authModule,
    categoriesModule,
    productsModule,
    sellersModule,
    shoppingCartModule
  }
});
