<template>
  <div class="login">
    <h2>Login</h2>
    <form>
      <b-field label="Username">
        <b-input v-model="username" />
      </b-field>
      <b-field label="Password">
        <b-input v-model="password" type="password" password-reveal />
      </b-field>
      <b-button @click.prevent="login">Login</b-button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    login() {
      let username = this.username;
      let password = this.password;
      this.$store
        .dispatch("login", { username, password })
        .then(() => this.$router.push("/"))
        .catch(() => {
          this.$buefy.notification.open({
            duration: 5000,
            message: `Username or password are incorrect. Try again or register.`,
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
  grid-gap: 1.5rem;
}

.form-forgot {
  text-align: center;
  font-size: 1.2rem;
  color: #64b5f6;
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
