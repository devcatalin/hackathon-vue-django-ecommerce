const saveToLocalStorage = (key, value) => {
  localStorage.setItem(key, JSON.stringify(value));
}

export const shoppingCartModule = {
  state: {
    cart: {
      items: [],
      total: 0
    }
  },
  getters: {
    cartItems: state => state.cart.items,
    cartTotal: state => state.cart.total
  },
  mutations: {
    getCart(state) {
      let cart = localStorage.getItem("cart");
      if (cart) {
        state.cart = JSON.parse(cart);
      }
    },
    addCartItem(state, item) {
      if (state.cart.items.includes(item))
        return;
      item.quantity = 1;
      state.cart.items = [...state.cart.items, item];
      state.cart.total = state.cart.total + item.price;
      saveToLocalStorage("cart", state.cart);
    },
    removeCartItem(state, product) {
      const first_length = state.cart.items.length;
      state.cart.items = state.cart.items.filter(i => {
        return i.slug !== product.slug;
      });
      const second_length = state.cart.items.length;
      if (first_length !== second_length) {
        state.cart.total = state.cart.total - product.price;
      }
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
    removeCartItem({ commit }, item) {
      console.log("ajunge aici", item);
      commit('removeCartItem', item);
    }
  }
}
