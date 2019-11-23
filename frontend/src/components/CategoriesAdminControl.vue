<template>
    <div class="categories p-l-xxl p-r-xxl m-b-lg">
        <div class="admin-category">
            <h1 class="m-b-md">Categorii</h1>
            <hr />
            <div
                class="cat-subcat-display m-b-md"
                v-for="category in categories"
                :key="category.title"
            >
                <button class="button" @click="setSelectedCategory(category)">
                    {{ category.title }}
                </button>
                <a @click="setCategoryDelete">
                    <b-icon
                        type="is-danger"
                        class="m-l-md"
                        icon="close"
                    ></b-icon>
                </a>
            </div>
            <div class="flex-center">
                <a v-if="!showCategoryInput" @click="setCategoryInput"
                    >Adaugati categorie noua</a
                >
                <b-field label="Nume categorie" v-else>
                    <b-input
                        icon="plus"
                        icon-clickable="true"
                        @icon-click="setCategoryInput"
                        @keyup.native.enter="setCategoryInput"
                    />
                </b-field>
            </div>
        </div>
        <div class="admin-subcategory">
            <h1 class="m-b-md">Subcategorii</h1>
            <hr />
            <div v-if="selectedCategory">
                <div
                    class="cat-subcat-display m-b-md"
                    v-for="subcategory in selectedCategory.subcategories"
                    :key="subcategory"
                >
                    <b-button>{{ subcategory.title }}</b-button>
                    <a @click="setSubcategoryDelete">
                        <b-icon
                            type="is-danger"
                            class="m-l-md"
                            icon="close"
                        ></b-icon>
                    </a>
                </div>
                <div class="flex-center">
                    <a v-if="!showSubcategoryInput" @click="setSubcategoryInput"
                        >Adaugati subcategorie noua</a
                    >

                    <b-field v-else label="Nume subcategorie">
                        <b-input
                            icon="plus"
                            icon-clickable="true"
                            @icon-click="setSubcategoryInput"
                            @keyup.native.enter="setSubcategoryInput"
                        />
                    </b-field>
                </div>
            </div>
        </div>

        <b-modal
            :active.sync="categoryDelete"
            has-modal-card
            :can-cancel="true"
        >
            <div class="card p-md modal-content">
                <h3 class="m-b-lg">
                    Sunteti siguri ca doriti sa stergeti aceasta categorie?
                </h3>
                <div class="flex-align">
                    <b-button type="is-primary" @click="setCategoryDelete"
                        >Anuleaza</b-button
                    >
                    <b-button type="is-danger">Confirma</b-button>
                </div>
            </div>
        </b-modal>
        <b-modal
            :active.sync="subcategoryDelete"
            has-modal-card
            :can-cancel="true"
        >
            <div class="card p-md modal-content">
                <h3 class="m-b-lg">
                    Sunteti siguri ca doriti sa stergeti aceasta subcategorie?
                </h3>
                <div class="flex-align">
                    <b-button type="is-primary" @click="setSubcategoryDelete"
                        >Anuleaza</b-button
                    >
                    <b-button type="is-danger">Confirma</b-button>
                </div>
            </div>
        </b-modal>
    </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
    computed: {
        ...mapGetters(["categories"])
    },
    data() {
        return {
            categoryDelete: false,
            subcategoryDelete: false,
            selectedCategory: null,
            showCategoryInput: false,
            showSubcategoryInput: false
        };
    },
    methods: {
        setSelectedCategory(category) {
            this.selectedCategory = category;
        },
        setCategoryInput() {
            this.showCategoryInput = !this.showCategoryInput;
        },
        setSubcategoryInput() {
            this.showSubcategoryInput = !this.showSubcategoryInput;
        },
        setCategoryDelete() {
            this.categoryDelete = !this.categoryDelete;
        },
        setSubcategoryDelete() {
            this.subcategoryDelete = !this.subcategoryDelete;
        }
    }
};
</script>

<style lang="scss" scoped>
.categories {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 3rem;
}
.cat-subcat-display {
    display: grid;
    grid-template-columns: repeat(2, min-content);
    justify-content: center;
    align-items: center;
}
h1 {
    font-size: 1.4rem;
    text-align: center;
}

a {
    text-align: center;
}

h3 {
    font-size: 1.3rem;
}
</style>
