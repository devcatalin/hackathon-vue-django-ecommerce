<template>
  <div class="login card">
    <form v-on:submit.prevent class="card p-lg">
      <b-field label="Nume de utilizator">
        <b-input v-model="username"></b-input>
      </b-field>
      <b-field label="Parola">
        <b-input v-model="password"></b-input>
      </b-field>
      <Button text="Autentificare" />
    </form>
  </div>
</template>

<script>
import Button from "@/components/Button.vue";

export default {
  components: {
    Button
  },
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

  height: 91vh;
}

h2 {
  font-size: 3rem;
}

form {
  display: grid;
  grid-template-columns: 25rem;
  grid-gap: 1rem;
}
</style>
