<template>
    <b-navbar type="is-primary" :spaced="true" :shadow="true" :fixed-top="true">
        <template slot="brand">
            <b-navbar-item tag="router-link" :to="{ path: '/home' }">
                <p>LocalGoods</p>
            </b-navbar-item>
        </template>
        <template slot="end" v-if="isAuthenticated">
            <router-link to="/login" exact v-slot="{ isActive, navigate }">
                <b-navbar-item @click="navigate" :active="isActive"
                    >Autentificare</b-navbar-item
                >
            </router-link>
            <router-link to="/register" exact v-slot="{ isActive, navigate }">
                <b-navbar-item @click="navigate" :active="isActive"
                    >Inregistrare</b-navbar-item
                >
            </router-link>
        </template>
        <template slot="end" v-else>
            <router-link to="/my-account" exact v-slot="{ isActive, navigate }">
                <b-navbar-item @click="navigate" :active="isActive"
                    >Contul meu</b-navbar-item
                >
            </router-link>
            <b-dropdown aria-role="menu" hoverable position="is-bottom-left">
                <b-button
                    slot="trigger"
                    type="is-primary"
                    to="/shopping-cart"
                    tag="router-link"
                >
                    <span>Cos de cumparaturi</span>
                    <b-icon icon="menu-down"></b-icon>
                </b-button>
                <b-dropdown-item custom aria-role="menuitem">
                    <div class="shopping-cart-dropdown">
                        <div>
                            <router-link to="/shopping-cart"
                                >{{ cartItems.length }} produse in
                                cos</router-link
                            >
                            <p>{{ sumCartItems }} Lei</p>
                        </div>
                        <b-button size="is-small" class="is-primary"
                            >Trimite comanda</b-button
                        >
                    </div>
                </b-dropdown-item>
            </b-dropdown>

            <router-link
                to="/seller-products"
                exact
                v-slot="{ isActive, navigate }"
            >
                <b-navbar-item v-if="isSeller" @click="navigate"
                    >Lista produse</b-navbar-item
                >
            </router-link>
            <router-link to="/home" exact v-slot="{ isActive, navigate }">
                <b-navbar-item @click="navigate">Deconectare</b-navbar-item>
            </router-link>
        </template>
    </b-navbar>
</template>

<script>
import { mapGetters } from "vuex";

export default {
    computed: {
        ...mapGetters(["isAuthenticated", "cartItems"]),
        sumCartItems() {
            let sum = 0;
            for (let i = 0; i < this.cartItems.length; i++) {
                sum += this.cartItems[i].price;
            }
            return sum;
        }
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
.navbar-active {
    background-color: white;
    color: green;
}
.shopping-cart-dropdown {
    display: grid;
    grid-template-columns: repeat(2, max-content);
    grid-gap: 1rem;
    align-items: center;
}

p {
    font-weight: 700;
    font-size: 1.1rem;
}

p {
    font-family: "Boogaloo", cursive;
    font-size: 1.8rem;
}
</style>
