<template>
  <div class="sidebar">
    <div v-if="!isAuthenticated" class="sidebar-links">
      <b-menu>
        <b-menu-list>
          <router-link to="/register" exact v-slot="{ isActive, navigate }">
            <b-menu-item @click="navigate" :active="isActive" icon="account" label="Register" />
          </router-link>
          <router-link to="/login" exact v-slot="{ isActive, navigate }">
            <b-menu-item @click="navigate" :active="isActive" icon="logout" label="Login" />
          </router-link>
        </b-menu-list>
      </b-menu>
    </div>
    <div v-else class="sidebar-links">
      <img src="/img/avatar.jpg" alt="userAvatar" />
      <b-menu>
        <b-menu-list>
          <router-link to="/account" exact v-slot="{ isActive, navigate }">
            <b-menu-item @click="navigate" :active="isActive" icon="account" label="My Account" />
          </router-link>
          <b-menu-item @click="logout" icon="logout" label="Logout"></b-menu-item>
        </b-menu-list>
      </b-menu>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["isAuthenticated"])
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push("/login");
    }
  }
};
</script>

<style scoped>
.menu-link a {
  color: white !important;
  font-size: 1.5rem;
}

.sidebar {
  position: fixed;
  z-index: 2000;
  width: 16%;
  height: 100%;
  box-shadow: 0 0 7px rgba(0, 0, 0, 0.1);
  padding-top: 10rem;
}

.sidebar-links {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.user-specs {
  font-size: 1.5rem;
}

img {
  border-radius: 50%;
  width: 6rem;
  height: 6rem;
  margin-bottom: 2.5rem;
}

/* a {
  font-size: 1.7rem;
  letter-spacing: 0.1rem;
  color: #fff;
}

a:after {
  display: block;
  content: "";
  border-bottom: solid 1px #fff;
  transform: scaleX(0);
  transition: all 0.4s ease-in-out;
}

a:hover {
  color: white;
}

a:hover:after {
  transform: scaleX(1);
} */

.sidebar-active-link {
  color: #40306d;
}

.sidebar-active-link:hover {
  color: #40306d;
}

.sidebar-active-link:after {
  border-bottom: solid 1px #40306d;
}

@media only screen and (max-width: 1150px) {
  .sidebar {
    height: 5rem;
    width: 100%;
    grid-template-rows: 1fr;
    justify-items: start;
    align-items: center;
    padding: 0 2rem;
  }
  .sidebar-links {
    display: grid;
    grid-template-columns: repeat(2, min-content);
    grid-column-gap: 2rem;
  }
  a {
    font-size: 1.3rem;
  }
}
</style>
