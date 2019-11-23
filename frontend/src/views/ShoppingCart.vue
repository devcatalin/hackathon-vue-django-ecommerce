<template>
    <div class="shopping-cart m-l-lg m-r-lg m-t-lg">
        <div class="m-b-lg">
            <b-table :bordered="true" :data="data">
                <template slot-scope="props">
                    <b-table-column field="name" label="Nume produs">{{
                        props.row.name
                    }}</b-table-column>
                    <b-table-column field="category" label="Categorie">{{
                        props.row.category
                    }}</b-table-column>
                    <b-table-column
                        width="200"
                        field="subcategory"
                        label="Subcategorie"
                        >{{ props.row.subcategory }}</b-table-column
                    >
                    <b-table-column field="u_m" label="U.M.">{{
                        props.row.u_m
                    }}</b-table-column>
                    <b-table-column
                        field="cantity"
                        label="Cantitate"
                        width="250"
                    >
                        <b-field>
                            <b-numberinput
                                controls-position="compact"
                                min="0"
                                v-model="props.row.cantity"
                            ></b-numberinput>
                        </b-field>
                    </b-table-column>
                    <b-table-column centered field="price" label="Pret">{{
                        props.row.price
                    }}</b-table-column>
                    <b-table-column width="50" field="price">
                        <a @click="deleteProduct = true">
                            <b-icon type="is-danger" icon="delete"></b-icon>
                        </a>
                    </b-table-column>
                </template>
            </b-table>
        </div>
        <h4 class="level-right">Total cos: 5,800.00 Lei</h4>
        <h4 class="level-right m-b-sm">Cost livrare: {{ deliveryCost }} Lei</h4>
        <h2 class="level-right">Total de plata: 5,810.70 Lei</h2>

        <div class="card m-t-lg p-lg payment-panel">
            <h1>Doresc sa mi se livreze comanda la:</h1>
            <div class="field">
                <b-radio
                    native-value="oldAddress"
                    v-model="address"
                    name="address"
                    size="is-medium"
                    >Adresa</b-radio
                >
            </div>
            <div class="field">
                <b-radio
                    name="address"
                    native-value="newAddress"
                    v-model="address"
                    size="is-medium"
                    >Adauga adresa noua</b-radio
                >
            </div>
            <div v-if="address == 'newAddress'" class="full-columns m-b-md">
                <label class="label">Adresa</label>
                <address-search />
            </div>
        </div>
        <div class="payment-panel card p-lg m-t-lg m-b-md">
            <h1>Plata cu cardul</h1>
            <card
                class="stripe-card m-b-md"
                :class="{ complete }"
                stripe="pk_test_XXXXXXXXXXXXXXXXXXXXXXXX"
                @change="setComplete"
            />
            <b-button class="pay-with-stripe" :disabled="!complete">
                Plateste acum
            </b-button>
        </div>

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
import { Card } from "vue-stripe-elements-plus";
import AddressSearch from "../components/AddressSearch.vue";
export default {
    components: {
        Card,
        AddressSearch
    },
    data() {
        return {
            complete: false,
            deleteProduct: false,
            address: "oldAddress",
            deliveryCost: (
                0.05 * this.distance(45.7538, 21.2257, 46.7693, 23.5901, "K")
            ).toFixed(2),
            data: [
                {
                    name: "Rosii roz",
                    category: "Legume",
                    subcategory: "Rosii",
                    u_m: "KG",
                    cantity: 107,
                    price: "5 Lei"
                },
                {
                    name: "Cartofi albi",
                    category: "Legume",
                    subcategory: "Cartofi",
                    u_m: "KG",
                    cantity: 513,
                    price: "1.5 Lei"
                },
                {
                    name: "Rosii cherry",
                    category: "Legume",
                    subcategory: "Rosii",
                    u_m: "KG",
                    cantity: 55,
                    price: "9 Lei"
                },
                {
                    name: "Ardei Kapia",
                    category: "Legume",
                    subcategory: "Ardei",
                    u_m: "KG",
                    cantity: 89,
                    price: "6 Lei"
                },
                {
                    name: "Telina",
                    category: "Legume",
                    subcategory: "Telina",
                    u_m: "Buc",
                    cantity: 40,
                    price: "3 Lei"
                }
            ]
        };
    },
    methods: {
        setComplete(event) {
            this.complete = event.complete;
        },
        distance(lat1, lon1, lat2, lon2, unit) {
            if (lat1 == lat2 && lon1 == lon2) {
                return 0;
            } else {
                var radlat1 = (Math.PI * lat1) / 180;
                var radlat2 = (Math.PI * lat2) / 180;
                var theta = lon1 - lon2;
                var radtheta = (Math.PI * theta) / 180;
                var dist =
                    Math.sin(radlat1) * Math.sin(radlat2) +
                    Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
                if (dist > 1) {
                    dist = 1;
                }
                dist = Math.acos(dist);
                dist = (dist * 180) / Math.PI;
                dist = dist * 60 * 1.1515;
                if (unit == "K") {
                    dist = dist * 1.609344;
                }
                if (unit == "N") {
                    dist = dist * 0.8684;
                }
                return dist;
            }
        }
    }
};
</script>

<style lang="scss" scoped>
.shopping-cart {
    min-height: 100vh;
}
h2 {
    font-size: 1.3rem;
    font-weight: 700;
}

h3 {
    font-size: 1.5rem;
}

.flex-align {
    display: flex;
    justify-content: space-between;
}

h1 {
    font-size: 1.5rem;
    font-weight: 600;
}

.stripe-card {
    width: 300px;
    font-size: 1.4rem;
}

.payment-panel {
    display: grid;
    justify-items: center;
    grid-gap: 1rem;
}

.pay-with-stripe {
    background-color: #4caf50;
    color: #fff;
}
</style>
