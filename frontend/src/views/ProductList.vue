<template>
    <div class="home-main p-t-lg p-l-sm">
        <span></span>
        <div class="sorting-panel m-b-sm">
            <span class="m-r-sm">Ordoneaza dupa:</span>
            <b-dropdown
                v-model="selectedSortOption"
                aria-role="list"
                class="m-r-lg"
            >
                <button class="button is-primary" type="button" slot="trigger">
                    <template>
                        <span>{{ selectedSortOption.label }}</span>
                    </template>
                    <b-icon icon="menu-down"></b-icon>
                </button>
                <b-dropdown-item
                    v-for="sortOption in sortOptions"
                    :key="sortOption.slug"
                    :value="sortOption"
                    aria-role="listitem"
                    >{{ sortOption.label }}</b-dropdown-item
                >
            </b-dropdown>
            <span class="m-r-sm">Tip afisare:</span>
            <b-dropdown aria-role="list" v-model="viewOption" class="z-index">
                <button class="button is-primary" type="button" slot="trigger">
                    <template v-if="viewOption === 'Grid'">
                        <span>Grid</span>
                    </template>
                    <template v-else-if="viewOption === 'List'">
                        <span>List</span>
                    </template>
                    <template v-else>
                        <span>Harta</span>
                    </template>
                    <b-icon icon="menu-down"></b-icon>
                </button>

                <b-dropdown-item value="Grid" aria-role="listitem"
                    >Grid</b-dropdown-item
                >
                <b-dropdown-item value="List" aria-role="listitem"
                    >Lista</b-dropdown-item
                >
                <b-dropdown-item value="Harta" aria-role="listitem"
                    >Harta</b-dropdown-item
                >
            </b-dropdown>
        </div>

        <sidebar />
        <div class="grid-view" v-if="viewOption === 'Grid'">
            <product-grid
                v-for="product in products"
                :key="product.slug"
                :product="product"
            />
        </div>
        <div v-else-if="viewOption === 'List'">
            <product-list
                v-for="product in products"
                :key="product.slug"
                :product="product"
            />
        </div>
        <map-view v-else />
    </div>
</template>

<script>
import Sidebar from "../components/Sidebar.vue";
import ProductGrid from "../components/ProductGridItem.vue";
import ProductList from "../components/ProductListItem.vue";
import MapView from "../components/MapView.vue";

import { mapGetters } from "vuex";

export default {
    components: { Sidebar, ProductGrid, ProductList, MapView },
    data() {
        return {
            viewOption: "Grid",
            sortOptions: [
                {
                    label: "Pret crescator",
                    slug: "price"
                },
                {
                    label: "Pret descrescator",
                    slug: "-price"
                },
                {
                    label: "Titlu A-Z",
                    slug: "title"
                },
                {
                    label: "Titlu Z-A",
                    slug: "-title"
                },
                {
                    label: "Vanzatori A-Z",
                    slug: "owner__profile__full_name"
                },
                {
                    label: "Vanzatori Z-A",
                    slug: "-owner__profile__full_name"
                }
            ],
            selectedSortOption: {
                label: "Pret crescator",
                slug: "price"
            }
        };
    },
    computed: {
        ...mapGetters(["products"])
    },
    beforeMount() {
        this.$store.dispatch("fetchProducts");
    },
    watch: {
        selectedSortOption() {
            this.$store.dispatch("setFilters", {
                sort: this.selectedSortOption.slug
            });
        }
    }
};
</script>

<style>
.home-main {
    min-height: 100vh;
    display: grid;
    grid-template-columns: 15rem 1fr;
    grid-column-gap: 2rem;
    grid-row-gap: 0.8rem;
}

.sorting-panel {
    display: flex;
    align-items: center;
}

i {
    cursor: pointer;
}

.z-index {
    z-index: 20;
}

.grid-view {
    display: grid;
    /* grid-template-columns: repeat(auto-fit, minmax(18rem, 1fr)); */
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: min-content;
    grid-row-gap: 4rem;
    grid-column-gap: 2rem;
}
</style>
