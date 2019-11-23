import http from "@/http";

export const authModule = {
  state: {
    token: localStorage.getItem("token") || "",
    user: {
      username: "",
      email: "",
      profile: {
        user_type: "",
        full_name: "",
        phone_number: "",
        address: "",
        buyer_type: ""
      }
    }
  },
  getters: {
    isAuthenticated: state => !!state.token,
    isSeller: state => state.user.profile.user_type === "seller",
    user: state => state.user
  },
  mutations: {
    auth_success(state, token) {
      state.token = token;
    },
    logout(state) {
      state.token = "";
    },
    setUserData(state, user) {
      state.user = user;
    }
  },
  actions: {
    async fetchUserData({ commit }) {
      commit("loading", true);
      const response = await http.get("/api/users/profile/detail/");
      commit("loading", false);
      commit("setUserData", response.data);
    },
    login({ commit }, payload) {
      const { username, password } = payload;
      return new Promise((resolve, reject) => {
        commit("loading", true);
        http
          .post("/api/users/token/", {
            username,
            password
          })
          .then(response => {
            const token = response.data.access;
            localStorage.setItem("token", token);
            commit("auth_success", token);
            commit("loading", false);
            resolve(response);
          })
          .catch(err => {
            commit("loading", false);
            localStorage.removeItem("token");
            reject(err);
          });
      });
    },
    register({ commit }, payload) {
      console.log(payload);
      // const {
      //   username,
      //   user_type,
      //   email,
      //   full_name,
      //   phone_number,
      //   address,
      //   latitude,
      //   longitude,
      //   password,
      //   buyer_type
      // } = payload;
      return new Promise((resolve, reject) => {
        commit("loading", true);
        http
          .post("/api/users/register/", {
            ...payload
            // username,
            // user_type,
            // email,
            // full_name,
            // phone_number,
            // address,
            // latitude,
            // longitude,
            // password,
            // buyer_type
          })
          .then(() => {
            commit("loading", false);
            resolve();
          })
          .catch(() => {
            commit("loading", false);
            reject();
          });
      });
    },
    logout({ commit }) {
      localStorage.removeItem("token");
      commit("logout");
    }
  }
};

// return new Promise((resolve, reject) => {
//     commit('loading', true);
//     axios.post("", {

//     }).then(response => {
//       commit("loading", false);
//       const { questions } = response.data;
//       commit("setQuestions", questions);
//       // ce faci cu raspunsu?
//       resolve();
//     }).catch(error => {
//       commit("loading", false);
//       // ce faci cu eroarea?
//       reject();
//     })
//   }
// )
