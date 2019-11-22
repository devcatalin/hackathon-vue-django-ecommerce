const saveToLocalStorage = (key, value) => {
  localStorage.setItem(key, JSON.stringify(value));
}

export const shoppingCartModule = {
  state: {
    cart: {
      items: []
    }
  },
  getters: {
    cartItems: state => state.cart.items
  },
  mutations: {
    getCart(state) {
      let cart = localStorage.getItem("cart");
      if (cart) {
        state.cart = JSON.parse(cart);
      }
    },
    addCartItem(state, item) {
      state.cart.items = [...state.cart.items, item];
      saveToLocalStorage("cart", state.cart);
    },
    removeCartItem(state, item_slug) {
      state.cart.items = state.cart.items.filter(item => item.slug !== item_slug)
      saveToLocalStorage("cart", state.cart);
    }
  },
  actions: {
    getCart({ commit }) {
      commit('getCart');
    },
    addCartItem({ commit }, item) {
      commit('addCartItem', item);
    },
    removeCartItem({ commit }, item_slug) {
      commit('removeCartItem', item_slug)
    }
  }
}
