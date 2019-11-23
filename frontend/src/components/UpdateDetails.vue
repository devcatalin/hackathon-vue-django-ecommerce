<template>
    <div class="product-create ">
        <form v-on:submit.prevent class="card p-lg">
            <b-field label="Nume">
                <b-input type="text" v-model="name"></b-input>
            </b-field>
            <b-field label="Număr de telefon" message="Format: 0123-456-789">
                <b-input
                    v-model="phone_number"
                    type="tel"
                    pattern="[0-9]{4}-[0-9]{3}-[0-9]{3}"
                    required
                />
            </b-field>
            <b-field label="Email">
                <b-input v-model="email" type="email" required />
            </b-field>
            <div class="full-columns m-b-md">
                <label class="label">Adresă</label>
                <address-search @change="updateAddress" />
            </div>
            <button class="button is-primary" type="submit">Salvează</button>
        </form>
    </div>
</template>

<script>
import AddressSearch from "./AddressSearch.vue";

export default {
    components: {
        AddressSearch
    },
    data() {
        return {
            name: "",
            phone_number: "",
            email: "",
            address: ""
        };
    },
    methods: {
        updateAddress(event) {
            const { value, latlng } = event.suggestion;
            this.address = value;
            this.latitude = latlng.lat;
            this.longitude = latlng.lng;
        }
    }
};
</script>

<style lang="scss" scoped>
.product-create {
    display: grid;
    grid-gap: 2rem;
    justify-items: center;
    align-content: center;

    height: 96vh;
}

form {
    display: grid;
    grid-template-columns: 25rem;
    grid-gap: 1rem;
}
</style>
