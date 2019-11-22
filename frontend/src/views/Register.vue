<template>
  <div class="login">
    <h2>Register</h2>
    <form>
      <b-field label="Username" type>
        <b-input v-model="username" />
      </b-field>
      <b-field label="Email">
        <b-input type="email" v-model="email" />
      </b-field>
      <b-field label="Password">
        <b-input type="password" v-model="password" password-reveal />
      </b-field>
      <b-field label="Confirm password" :type="confirmPasswordValid" :message="passwordMessage">
        <b-input type="password" v-model="confirmPassword" />
      </b-field>
      <b-button @click="register">Register</b-button>
    </form>
  </div>
</template>

<script>
export default {
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
.login {
  display: grid;
  grid-template-rows: repeat(2, min-content);
  grid-gap: 3rem;
  justify-items: center;
  align-content: center;

  height: 100vh;
}

h2 {
  font-size: 3.4rem;
}

form {
  display: grid;
  grid-template-columns: 25rem;
  grid-gap: 1rem;
}

input {
  width: 25rem;
  height: 2.3rem;
  background: #fcfcfc;
  display: block;
  padding: 0.5rem;
  border: 1px solid #e7e7e7;
  border-radius: 0.3rem;
  font-size: 1rem;
}
</style>
