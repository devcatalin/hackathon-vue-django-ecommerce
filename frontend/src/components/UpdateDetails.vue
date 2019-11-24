<template>
  <div class="product-create">
    <form v-on:submit.prevent="updateProfile" class="card p-lg">
      <b-field label="Nume complet">
        <b-input type="text" :placeholder="user.profile.full_name" v-model="full_name"></b-input>
      </b-field>
      <b-field label="Număr de telefon" message="Format: 0123-456-789">
        <b-input
          :placeholder="user.profile.phone_number"
          v-model="phone_number"
          type="tel"
          pattern="[0-9]{4}-[0-9]{3}-[0-9]{3}"
        />
      </b-field>
      <b-field label="Email">
        <b-input :placeholder="user.email" v-model="email" type="email" />
      </b-field>
      <div class="full-columns m-b-md">
        <label class="label">Adresă</label>
        <address-search :required="false" @change="updateAddress" />
      </div>
      <button class="button is-primary" type="submit">Salvează</button>
    </form>
  </div>
</template>

<script>
import AddressSearch from "./AddressSearch.vue";
import { mapGetters } from "vuex";

export default {
  components: {
    AddressSearch
  },
  props: ["closeModal"],
  data() {
    return {
      full_name: "",
      phone_number: "",
      email: "",
      address: "",
      longitude: -1,
      latitude: -1
    };
  },
  computed: {
    ...mapGetters(["user"])
  },
  methods: {
    updateAddress(event) {
      const { value, latlng } = event.suggestion;
      this.address = value;
      this.latitude = latlng.lat;
      this.longitude = latlng.lng;
    },
    updateProfile() {
      this.$store.dispatch("updateProfile", {
        full_name: this.full_name,
        phone_number: this.phone_number,
        email: this.email,
        address: this.address,
        longitude: this.longitude,
        latitude: this.latitude
      });
      this.closeModal();
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
