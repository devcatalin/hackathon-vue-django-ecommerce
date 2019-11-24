<template>
    <div v-if="cartItems.length === 0">
        <div class="card">
            <div class="card-content">
                <h1 style="text-align: center;">Nu ai adăugat nimic in coș!</h1>
                <router-link
                    to="/products"
                    class="button is-large is-primary"
                    style="margin: 1rem auto; display: block; width: 50%;"
                    >Explorează</router-link
                >
            </div>
        </div>
    </div>
    <div v-else class="shopping-cart m-l-lg m-r-lg m-t-lg">
        <div class="m-b-lg">
            <b-table :bordered="true" :data="tableItems">
                <template slot-scope="props">
                    <b-table-column field="name" label="Nume produs">
                        {{ props.row.title }}
                    </b-table-column>
                    <b-table-column field="category" label="Categorie">
                        {{ props.row.category.title }}
                    </b-table-column>
                    <b-table-column
                        width="200"
                        field="subcategory"
                        label="Subcategorie"
                        >{{ props.row.subcategory.title }}</b-table-column
                    >
                    <b-table-column field="u_m" label="U.M.">
                        {{ props.row.quantity_type }}
                    </b-table-column>
                    <b-table-column
                        field="cantity"
                        label="Cantitate"
                        width="250"
                    >
                        <b-field>
                            <b-numberinput
                                controls-position="compact"
                                min="1"
                                :max="props.row.quantity"
                                v-model="props.row.cart_quantity"
                            ></b-numberinput>
                        </b-field>
                    </b-table-column>
                    <b-table-column centered field="price" label="Preț">
                        {{ props.row.price }}
                    </b-table-column>
                    <b-table-column width="50" field="price">
                        <a
                            @click="
                                showDeleteProductModal(
                                    props.row.slug,
                                    props.row.price
                                )
                            "
                        >
                            <b-icon type="is-danger" icon="delete"></b-icon>
                        </a>
                    </b-table-column>
                </template>
            </b-table>
        </div>
        <h4 class="level-right">Total coș: {{ getCartTotal }} Lei</h4>
        <h4 class="level-right m-b-sm">Cost livrare: {{ deliveryCost }} Lei</h4>
        <h2 class="level-right">Total de plată: {{ getTotalCost }} Lei</h2>

        <div class="card m-t-lg p-lg payment-panel">
            <h1>Doresc să mi se livreze comanda la:</h1>
            <div class="field">
                <b-radio
                    native-value="oldAddress"
                    v-model="address"
                    name="address"
                    size="is-medium"
                    @click.native="setDefaultAddress"
                    >{{ user.profile.address }}</b-radio
                >
            </div>
            <div class="field">
                <b-radio
                    name="address"
                    native-value="newAddress"
                    v-model="address"
                    size="is-medium"
                    >Adaugă adresă nouă</b-radio
                >
            </div>
            <div
                style="width: 30rem"
                v-if="address == 'newAddress'"
                class="m-b-md"
            >
                <label class="label">Adresă</label>
                <address-search @change="onAddressChange" :required="true" />
            </div>
        </div>
        <div class="payment-panel card p-lg m-t-lg m-b-md">
            <h1>Plată cu cardul</h1>
            <card
                class="stripe-card m-b-md"
                :class="{ complete }"
                stripe="pk_test_NGsJ3Z68VDy1wJRWckevqlPb00fSf5vdIa"
                @change="setComplete"
            />
            <b-button class="pay-with-stripe" :disabled="!complete" @click="pay"
                >Plătește acum</b-button
            >
        </div>

        <b-modal
            :active.sync="deleteProductModal.visible"
            has-modal-card
            :can-cancel="true"
        >
            <div class="card p-md modal-content">
                <h3 class="m-b-lg">
                    Sunteți siguri că doriți să ștergeți acest produs?
                </h3>
                <div class="flex-align">
                    <b-button type="is-primary" @click="cancelDeleteProduct"
                        >Anulează</b-button
                    >
                    <b-button type="is-danger" @click="deleteProductFromCart"
                        >Confirmă</b-button
                    >
                </div>
            </div>
        </b-modal>
    </div>
</template>

<script>
import { Card, createToken } from "vue-stripe-elements-plus";
import AddressSearch from "../components/AddressSearch.vue";

import http from "@/http";

import { mapGetters } from "vuex";

export default {
    components: {
        Card,
        AddressSearch
    },
    data() {
        return {
            complete: false,
            deleteProductModal: {
                visible: false,
                product: null
            },
            address: "oldAddress",
            userAddress: {
                name: "",
                longitude: 0,
                latitude: 0
            },
            tableItems: []
        };
    },
    beforeMount() {
        this.tableItems = [...this.cartItems];
        this.setDefaultAddress();
    },
    computed: {
        ...mapGetters(["cartItems", "user"]),
        getCartTotal() {
            let sum = 0;
            for (let i = 0; i < this.tableItems.length; i++) {
                const item = this.tableItems[i];
                sum += item.cart_quantity * item.price;
            }
            return sum;
        },
        deliveryCost() {
            let sum = 0;
            let distances = {};
            for (let i = 0; i < this.tableItems.length; i++) {
                let item = this.tableItems[i];
                if (item.seller in distances) {
                    continue;
                }
                distances[item.seller] = item.seller;
                let distance = this.distance(
                    this.userAddress.latitude,
                    this.userAddress.longitude,
                    item.seller_latitude,
                    item.seller_longitude
                );
                sum += distance;
            }
            let avg = sum / this.tableItems.length;
            return (0.05 * avg).toFixed(2);
        },
        getTotalCost() {
            return (
                parseFloat(this.getCartTotal) + parseFloat(this.deliveryCost)
            ).toFixed(2);
        }
    },
    methods: {
        async pay() {
            const cardResponse = await createToken();
            const card_token = JSON.stringify(cardResponse.token);
            console.log(card_token);
            let summary = "";
            for (let i = 0; i < this.tableItems.length; i++) {
                let item = this.tableItems[i];
                summary += `${item.title} x ${item.cart_quantity} - `;
            }
            summary = summary.slice(0, -3);

            const item_quantities = this.tableItems.map(item => {
                return {
                    slug: item.slug,
                    cart_quantity: item.cart_quantity
                };
            });

            console.log(item_quantities);

            await http.post("/api/shop/invoices/create/", {
                card_token: card_token,
                total_cost: this.getTotalCost,
                summary,
                billing_address: this.user.profile.address,
                shipping_address: this.userAddress.name,
                item_quantities: item_quantities
            });

            this.$store.dispatch("clearCart");

            this.$router.push("/my-account");

            this.$buefy.toast.open("Comanda a fost trimisă cu success!");
        },
        setDefaultAddress() {
            this.userAddress.name = this.user.profile.address;
            this.userAddress.latitude = this.user.profile.latitude;
            this.userAddress.longitude = this.user.profile.longitude;
        },
        onAddressChange(event) {
            if (event.suggestion.value) {
                this.userAddress.name = event.suggestion.value;
                this.userAddress.latitude = event.suggestion.latlng.lat;
                this.userAddress.longitude = event.suggestion.latlng.lng;
            }
        },
        cancelDeleteProduct() {
            this.deleteProductModal = {
                visible: false,
                product: null
            };
        },
        showDeleteProductModal(item_slug, item_price) {
            this.deleteProductModal = {
                visible: true,
                product: {
                    slug: item_slug,
                    price: item_price
                }
            };
        },
        deleteProductFromCart() {
            this.$store.dispatch("removeCartItem", {
                ...this.deleteProductModal.product
            });
            this.tableItems = this.tableItems.filter(
                i => i.slug !== this.deleteProductModal.product.slug
            );
            this.cancelDeleteProduct();
        },
        setComplete(event) {
            this.complete = event.complete;
        },
        distance(lat1, lon1, lat2, lon2) {
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

                return dist * 1.609344;
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
