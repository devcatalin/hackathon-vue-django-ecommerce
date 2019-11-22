<template>
  <form class="card p-lg">
    <div class="inputs">
      <b-field label="Nume">
        <b-input v-model="name"></b-input>
      </b-field>
      <b-field label="Numar de telefon" type="is-info" message="Format: 0123-456-789">
        <b-input type="tel" pattern="[0-9]{4}-[0-9]{3}-[0-9]{3}" required></b-input>
      </b-field>
      <b-field label="Email">
        <b-input type="email"></b-input>
      </b-field>
      <b-field label="Adresa">
        <b-input type="text"></b-input>
      </b-field>
      <b-field label="Parola">
        <b-input type="password" v-model="password" password-reveal></b-input>
      </b-field>
      <b-field label="Confirmare parola" :type="confirmPasswordValid" :message="passwordMessage">
        <b-input type="password" v-model="confirmPassword"></b-input>
      </b-field>
    </div>
    <b-field label="Ce tip de vanzator esti">
      <div class="block">
        <b-radio v-model="radio" name="type" native-value="Private">Privat</b-radio>
        <b-radio v-model="radio" name="type" native-value="Company">Companie</b-radio>
      </div>
    </b-field>
    <Button text="Register" />
  </form>
</template>

<script>
import Button from "@/components/Button.vue";
export default {
  components: {
    Button
  }
};
</script>

<style lang="scss" scoped>
.inputs {
  display: grid;
  grid-template-columns: repeat(2, 25rem);
  grid-column-gap: 1rem;
}
</style>