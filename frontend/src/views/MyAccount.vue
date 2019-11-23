<template>
    <div class="my-account m-t-xl p-lg">
        <div class="card m-b-lg p-lg">
            <h1 class="m-b-md">Detalii cont</h1>
            <div v-for="(value, key) in userData" :key="value">
                <h2 class="m-b-sm">
                    {{ key }}: <span>{{ value }}</span>
                </h2>
            </div>
            <div class="flex-center">
                <b-button @click="updateInfo = true" type="is-primary"
                    >Editeaza informatiile</b-button
                >
            </div>
        </div>
        <div class="card orders-card p-lg">
            <h1 class="m-b-lg">Comenzile mele</h1>
            <b-table
                :data="data"
                ref="table"
                :opened-detailed="defaultOpenedDetails"
                detailed
                detail-key="id"
                :show-detail-icon="showDetailIcon"
            >
                <template slot-scope="props">
                    <b-table-column field="id" label="ID" width="40" numeric>
                        {{ props.row.id }}
                    </b-table-column>

                    <b-table-column centered field="date" label="Date">
                        <template v-if="showDetailIcon">
                            {{ props.row.date }}
                        </template>
                        <template v-else>
                            <a @click="toggle(props.row)">
                                {{ props.row.date }}
                            </a>
                        </template>
                    </b-table-column>

                    <b-table-column
                        centered
                        field="number_of_products"
                        label="Numar produse"
                    >
                        {{ props.row.number_of_products }}
                    </b-table-column>

                    <b-table-column
                        centered
                        field="total"
                        label="Total comanda"
                    >
                        {{ props.row.total }}
                    </b-table-column>
                </template>

                <template slot="detail">
                    <div class="order-details">
                        <b-table :data="orderData">
                            <template slot-scope="props">
                                <b-table-column
                                    field="name"
                                    label="Nume produs"
                                >
                                    {{ props.row.name }}
                                </b-table-column>
                                <b-table-column
                                    field="u_m"
                                    label="Unitate de masura"
                                >
                                    {{ props.row.u_m }}
                                </b-table-column>
                                <b-table-column
                                    field="cantity"
                                    label="Cantitate"
                                >
                                    {{ props.row.cantity }}
                                </b-table-column>
                                <b-table-column
                                    field="price"
                                    label="Pret total"
                                >
                                    {{ props.row.price }}
                                </b-table-column>
                            </template>
                        </b-table>
                    </div>
                </template>
            </b-table>
        </div>
        <b-modal :active.sync="updateInfo" has-modal-card :can-cancel="true">
            <update-details />
        </b-modal>
    </div>
</template>

<script>
import UpdateDetails from "../components/UpdateDetails.vue";

export default {
    components: {
        UpdateDetails
    },
    methodes: {
        toggle(row) {
            this.$refs.table.toggleDetails(row);
        }
    },
    data() {
        return {
            deleteOrder: false,
            updateInfo: false,
            defaultOpenedDetails: [],
            showDetailIcon: true,
            data: [
                {
                    id: 1,
                    date: "2016/10/15 13:43:27",
                    number_of_products: 3,
                    total: "5,823 Lei"
                },
                {
                    id: 2,
                    date: "2016/10/15 13:43:27",
                    number_of_products: 3,
                    total: "5,823 Lei"
                },
                {
                    id: 3,
                    date: "2016/10/15 13:43:27",
                    number_of_products: 3,
                    total: "5,823 Lei"
                },
                {
                    id: 4,
                    date: "2016/10/15 13:43:27",
                    number_of_products: 3,
                    total: "5,823 Lei"
                },
                {
                    id: 5,
                    date: "2016/10/15 13:43:27",
                    number_of_products: 3,
                    total: "5,823 Lei"
                }
            ],
            orderData: [
                {
                    name: "Rosii",
                    u_m: "KG",
                    cantity: 50,
                    price: "512 Lei"
                },
                {
                    name: "Cartofi",
                    u_m: "KG",
                    cantity: 102,
                    price: "255 Lei"
                }
            ],
            userData: {
                Name: "Razvan",
                Phone_number: "0720 123 456",
                Email: "razvan@gmail.com",
                Address: "Strada exemplu"
            }
        };
    }
};
</script>

<style lang="scss" scoped>
.my-account {
    min-height: 100vh;
}
h1 {
    font-size: 2rem;
    font-weight: 700;
    text-align: center;
}
.flex-align {
    display: flex;
    justify-content: space-between;
}
.flex-center {
    display: flex;
    justify-content: center;
}
h3 {
    font-size: 1.5rem;
}

.order-details {
    display: grid;
    grid-template-columns: 65%;
    justify-content: center;
}

.b-table .table tr.detail {
    background: green !important;
}

h2 {
    font-size: 1.4rem;
    font-weight: 700;
}
h2 span {
    font-size: 1.2rem;
    font-weight: 500;
}
</style>
