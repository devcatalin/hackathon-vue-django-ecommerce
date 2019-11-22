<template>
  <div class="register">
    <b-tabs type="is-boxed" expanded="true">
      <b-tab-item>
        <template slot="header">
          <b-icon icon="cart-plus"></b-icon>
          <span>Cumparator</span>
        </template>
        <register-form buyerTypeLabel="Ce tip de cumparator esti ?" />
      </b-tab-item>
      <b-tab-item>
        <template slot="header">
          <b-icon icon="account"></b-icon>
          <span>Vanzator</span>
        </template>
        <register-form buyerTypeLabel="Ce tip de cumparatori vrei sa ai ?" />
      </b-tab-item>
    </b-tabs>
  </div>
</template>

<script>
import RegisterForm from "../components/RegisterForm.vue";

export default {
  components: { RegisterForm },
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: ""
    };
  },
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
        return "Passwords does not match";
      }
      return "";
    }
  },
  methods: {
    register() {
      if (this.password !== this.confirmPassword) return;
      let username = this.username;
      let email = this.email;
      let password = this.password;
      this.$store
        .dispatch("register", {
          username,
          email,
          password
        })
        .then(() => {
          this.$router.push("/login");
        })
        .catch(() => {
          this.$buefy.notification.open({
            duration: 5000,
            message: `Username or email already exist.`,
            position: "is-bottom",
            type: "is-danger",
            hasIcon: true
          });
        });
    }
  }
};
</script>

<style scoped>
.register {
  display: grid;
  justify-content: center;
  justify-items: center;
  align-items: center;
  align-content: center;

  height: 85vh;
}

h2 {
  font-size: 3.4rem;
}

form {
  display: grid;
  justify-items: center;
  grid-row-gap: 1rem;
}
</style>
