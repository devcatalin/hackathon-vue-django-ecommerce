<template>
    <div class="card m-xl">
        <b-tabs :expanded="true" type="is-boxed">
            <b-tab-item label="Gestiune utilizatori">
                <users-admin-control />
            </b-tab-item>
            <b-tab-item label="Gestiune categorii">
                <categories-admin-control />
            </b-tab-item>
            <b-tab-item label="Gestiune anunturi">
                <products-admin-control />
            </b-tab-item>
        </b-tabs>
    </div>
</template>

<script>
import UsersAdminControl from "../components/UsersAdminControl";
import ProductsAdminControl from "../components/ProductsAdminControl";
import CategoriesAdminControl from "../components/CategoriesAdminControl";
export default {
    components: {
        UsersAdminControl,
        ProductsAdminControl,
        CategoriesAdminControl
    }
};
</script>

<style lang="scss" scoped></style>
