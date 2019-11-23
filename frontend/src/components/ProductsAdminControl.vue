<template>
    <div class="m-t-md p-lg">
        <b-table :data="data">
            <template slot-scope="props">
                <b-table-column field="name" label="Nume produs">{{
                    props.row.name
                }}</b-table-column>
                <b-table-column field="category" label="Categorie">{{
                    props.row.category
                }}</b-table-column>
                <b-table-column field="u_m" label="U.M.">{{
                    props.row.u_m
                }}</b-table-column>
                <b-table-column field="cantity" label="Cantitate">{{
                    props.row.cantity
                }}</b-table-column>
                <b-table-column field="price" label="Pret pe unitate"
                    >{{ props.row.price }} Lei</b-table-column
                >
                <b-table-column field="username" label="Nume utilizator">{{
                    props.row.username
                }}</b-table-column>
                <b-table-column width="50" field="price">
                    <a @click="setProductDelete">
                        <b-icon type="is-danger" icon="delete"></b-icon>
                    </a>
                </b-table-column>
            </template>
        </b-table>

        <b-modal :active.sync="productDelete" has-modal-card :can-cancel="true">
            <div class="card p-md modal-content">
                <h3 class="m-b-lg">
                    Sunteti siguri ca doriti sa stergeti acest anunt?
                </h3>
                <div class="flex-align">
                    <b-button type="is-primary" @click="setProductDelete"
                        >Anuleaza</b-button
                    >
                    <b-button type="is-danger">Confirma</b-button>
                </div>
            </div>
        </b-modal>

        <h2 class="m-t-xl level-right">Numar de anunturi: 1</h2>
    </div>
</template>

<script>
export default {
    data() {
        return {
            productDelete: false,
            data: [
                {
                    name: "Rosii roz",
                    category: "Legume",
                    u_m: "KG",
                    cantity: 107,
                    price: 5,
                    username: "Username"
                }
            ]
        };
    },
    methods: {
        setProductDelete() {
            this.productDelete = !this.productDelete;
        }
    }
};
</script>

<style lang="scss" scoped>
h2 {
    font-size: 1.5rem;
    font-weight: 600;
}

h3 {
    font-size: 1.3rem;
}
</style>
