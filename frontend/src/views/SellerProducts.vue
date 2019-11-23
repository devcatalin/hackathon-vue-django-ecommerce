<template>
    <div class="seller-products m-xl">
        <div class="flex-center">
            <b-button
                type="is-primary"
                class="m-b-lg flex-center"
                @click="updateProduct = true"
                >Adauga produs nou</b-button
            >
        </div>

        <div>
            <b-table bordered="true" :data="data">
                <template slot-scope="props">
                    <b-table-column
                        width="200"
                        field="name"
                        label="Nume produs"
                        >{{ props.row.name }}</b-table-column
                    >
                    <b-table-column field="description" label="Descriere">{{
                        props.row.description
                    }}</b-table-column>
                    <b-table-column
                        width="150"
                        field="category"
                        label="Categorie"
                        >{{ props.row.category }}</b-table-column
                    >
                    <b-table-column
                        width="150"
                        field="subcategory"
                        label="Subcategorie"
                        >{{ props.row.subcategory }}</b-table-column
                    >
                    <b-table-column width="80" field="u_m" label="U.M.">{{
                        props.row.u_m
                    }}</b-table-column>
                    <b-table-column
                        field="cantity"
                        label="Cantitate"
                        width="100"
                        >{{ props.row.cantity }}</b-table-column
                    >
                    <b-table-column
                        width="120"
                        centered
                        field="price"
                        label="Pret"
                        >{{ props.row.price }}</b-table-column
                    >
                    <b-table-column width="50" field="price">
                        <a @click="deleteProduct = true">
                            <b-icon type="is-danger" icon="delete"></b-icon>
                        </a>
                        <a @click="updateProduct = true">
                            <b-icon type="is-info" icon="pencil"></b-icon>
                        </a>
                    </b-table-column>
                </template>
            </b-table>
        </div>

        <b-modal :active.sync="updateProduct" has-modal-card :can-cancel="true">
            <product-create />
        </b-modal>
        <b-modal :active.sync="deleteProduct" has-modal-card :can-cancel="true">
            <div class="card p-md modal-content">
                <h3 class="m-b-lg">
                    Sunteti siguri ca doriti sa stergeti acest produs?
                </h3>
                <div class="flex-align">
                    <b-button type="is-primary" @click="deleteProduct = false"
                        >Anuleaza</b-button
                    >
                    <b-button type="is-danger">Confirma</b-button>
                </div>
            </div>
        </b-modal>
    </div>
</template>

<script>
import ProductCreate from "../views/ProductCreate.vue";

export default {
    components: {
        ProductCreate
    },
    data() {
        return {
            updateProduct: false,
            deleteProduct: false,
            addProducts: false,
            data: [
                {
                    name: "Rosii roz",
                    description:
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur pellentesque mollis lectus, et porttitor leo imperdiet et. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed mi arcu, euismod quis tortor in, tempor faucibus ligula. Aliquam vitae diam accumsan, placerat enim quis, eleifend neque.",
                    category: "Legume",
                    subcategory: "Rosii",
                    u_m: "KG",
                    cantity: "107",
                    price: "5 Lei"
                },
                {
                    name: "Cartofi albi",
                    category: "Legume",
                    subcategory: "Cartofi",
                    u_m: "KG",
                    cantity: "513",
                    price: "1.5 Lei"
                },
                {
                    name: "Rosii cherry",
                    category: "Legume",
                    subcategory: "Rosii",
                    u_m: "KG",
                    cantity: "55",
                    price: "9 Lei"
                },
                {
                    name: "Ardei Kapia",
                    category: "Legume",
                    subcategory: "Ardei",
                    u_m: "KG",
                    cantity: "89",
                    price: "6 Lei"
                },
                {
                    name: "Telina",
                    category: "Legume",
                    subcategory: "Telina",
                    u_m: "Buc",
                    cantity: "40",
                    price: "3 Lei"
                }
            ],
            columns: [
                {
                    field: "id",
                    label: "ID",
                    width: "40",
                    numeric: true
                },
                {
                    field: "first_name",
                    label: "First Name"
                },
                {
                    field: "last_name",
                    label: "Last Name"
                },
                {
                    field: "date",
                    label: "Date",
                    centered: true
                },
                {
                    field: "gender",
                    label: "Gender"
                }
            ]
        };
    }
};
</script>

<style lang="scss" scoped>
h3 {
    font-size: 1.5rem;
}

.flex-align {
    display: flex;
    justify-content: space-between;
}

.flex-center {
    display: flex;
    justify-content: center;
}
</style>
