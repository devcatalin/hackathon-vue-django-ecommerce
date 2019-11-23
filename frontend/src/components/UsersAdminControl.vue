<template>
    <div class="m-t-md p-lg">
        <b-table :data="data">
            <template slot-scope="props">
                <b-table-column field="name" label="Nume utlizator">{{
                    props.row.name
                }}</b-table-column>
                <b-table-column field="email" label="Email">{{
                    props.row.email
                }}</b-table-column>
                <b-table-column field="full_name" label="Nume">{{
                    props.row.full_name
                }}</b-table-column>
                <b-table-column field="phone_number" label="Numar de telefon">{{
                    props.row.phone_number
                }}</b-table-column>
                <b-table-column field="address" label="Adresa">{{
                    props.row.address
                }}</b-table-column>
                <b-table-column field="buyer_type" label="Tip utilizator">{{
                    props.row.buyer_type
                }}</b-table-column>
                <b-table-column width="50" field="price">
                    <a @click="setUserDelete">
                        <b-icon type="is-danger" icon="delete"></b-icon>
                    </a>
                </b-table-column>
            </template>
        </b-table>

        <b-modal :active.sync="userDelete" has-modal-card :can-cancel="true">
            <div class="card p-md modal-content">
                <h3 class="m-b-lg">
                    Sunteti siguri ca doriti sa stergeti acest utilizator?
                </h3>
                <div class="flex-align">
                    <b-button type="is-primary" @click="setUserDelete"
                        >Anuleaza</b-button
                    >
                    <b-button type="is-danger">Confirma</b-button>
                </div>
            </div>
        </b-modal>

        <h2 class="m-t-xl level-right">Numar de utilizatori: 1</h2>
    </div>
</template>

<script>
export default {
    data() {
        return {
            userDelete: false,
            data: [
                {
                    name: "username",
                    full_name: "Popescu Marian",
                    email: "popescu.marian@gmail.com",
                    phone_number: "0721-012-345",
                    address: "Strada Chisodei",
                    buyer_type: "Vanzator"
                }
            ]
        };
    },
    methods: {
        setUserDelete() {
            this.userDelete = !this.userDelete;
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
