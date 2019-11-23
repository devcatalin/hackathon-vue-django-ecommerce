<template>
  <form class="card p-lg" @submit.prevent="register">
    <div class="inputs">
      <b-field label="Nume de utilizator">
        <b-input v-model="username" required />
      </b-field>
      <b-field label="Email">
        <b-input v-model="email" type="email" required />
      </b-field>
      <b-field :label="fullNameLabel">
        <b-input v-model="full_name" type="text" required />
      </b-field>
      <b-field label="Număr de telefon" message="Format: 0123-456-789">
        <b-input v-model="phone_number" type="tel" pattern="[0-9]{4}-[0-9]{3}-[0-9]{3}" required />
      </b-field>

      <div class="full-columns m-b-md">
        <label class="label">Adresă</label>
        <address-search :required="true" @change="updateAddress" />
      </div>

      <!-- <b-field label="Adresa" class="full-columns">
        <b-input v-model="address" type="text" />
      </b-field>-->
      <b-field label="Parolă">
        <b-input type="password" v-model="password" password-reveal required />
      </b-field>
      <b-field label="Confirmare parolă" :type="confirmPasswordValid" :message="passwordMessage">
        <b-input type="password" v-model="confirmPassword" required />
      </b-field>
    </div>
    <b-field :label="buyerTypeLabel">
      <div class="block">
        <b-radio v-model="buyer_type" name="type" native-value="private" required>Privat</b-radio>
        <b-radio v-model="buyer_type" name="type" native-value="company" required>Companie</b-radio>
      </div>
    </b-field>
    <button class="button is-primary" type="submit">Înregistrează-te</button>
  </form>
</template>

<script>
import AddressSearch from "./AddressSearch.vue";

export default {
  data() {
    return {
      username: "",
      email: "",
      full_name: "",
      phone_number: "",
      address: "",
      latitude: "",
      longitude: "",
      password: "",
      buyer_type: "",
      confirmPassword: ""
    };
  },
  components: {
    AddressSearch
  },
  props: ["buyerTypeLabel", "fullNameLabel", "user_type"],
  computed: {
    confirmPasswordValid() {
      if (this.password === "") {
        return "";
      }
      if (this.password === this.confirmPassword) {
        return "is-success";
      }
      return "is-danger";
    },
    passwordMessage() {
      if (this.confirmPasswordValid == "is-danger") {
        return "Parolele trebuie sa fie la fel.";
      }
      return "";
    }
  },
  methods: {
    updateAddress(event) {
      const { value, latlng } = event.suggestion;
      this.address = value;
      this.latitude = latlng.lat;
      this.longitude = latlng.lng;
    },
    register() {
      if (this.password !== this.confirmPassword) return;
      let user_type = this.user_type;
      let username = this.username;
      let email = this.email;
      let password = this.password;
      let full_name = this.full_name;
      let phone_number = this.phone_number;
      let address = this.address;
      let latitude = this.longitude;
      let longitude = this.latitude;
      let buyer_type = this.buyer_type;
      this.$store
        .dispatch("register", {
          user_type,
          username,
          email,
          password,
          full_name,
          phone_number,
          address,
          latitude,
          longitude,
          buyer_type
        })
        .then(() => {
          this.$router.push("/login");
        })
        .catch(() => {
          this.$buefy.notification.open({
            duration: 5000,
            message: `There was an error. Try again later.`,
            position: "is-bottom",
            type: "is-danger",
            hasIcon: true
          });
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.inputs {
  display: grid;
  grid-template-columns: repeat(2, 25rem);
  grid-column-gap: 1rem;
}

.full-columns {
  grid-column: 1 / 3;
}
</style>
