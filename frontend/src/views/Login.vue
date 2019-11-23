<template>
    <div class="login card">
        <form v-on:submit.prevent="login" class="card p-lg">
            <b-field label="Nume de utilizator">
                <b-input v-model="username" required />
            </b-field>
            <b-field label="Parolă">
                <b-input
                    v-model="password"
                    type="password"
                    password-reveal
                    required
                />
            </b-field>
            <button type="submit" class="button is-primary">
                Autentificare
            </button>
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
                .then(() => {
                    this.$router.push("/");
                    this.$store.dispatch("fetchUserData");
                    this.$buefy.toast.open(`Bun venit, ${username} !`);
                })
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
