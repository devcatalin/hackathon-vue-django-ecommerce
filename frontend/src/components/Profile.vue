<template>
  <div>
    <div class="card m-b-lg p-lg">
      <h1 class="m-b-md">Detalii cont</h1>
      <h2 class="m-b-sm">
        Nume de utilizator:
        <span>{{ user.username }}</span>
      </h2>
      <h2 class="m-b-sm">
        Nume complet:
        <span>{{ user.profile.full_name }}</span>
      </h2>
      <h2 class="m-b-sm">
        Email:
        <span>{{ user.profile.email }}</span>
      </h2>
      <h2 class="m-b-sm">
        Număr de telefon:
        <span>{{ user.profile.phone_number }}</span>
      </h2>
      <h2 class="m-b-sm">
        Adresă:
        <span>{{ user.profile.address }}</span>
      </h2>
      <div class="flex-center">
        <b-button @click="updateInfo = true" type="is-primary">Editează informațiile</b-button>
      </div>
    </div>
    <b-modal :active.sync="updateInfo" has-modal-card :can-cancel="true">
      <update-details :closeModal="() => this.updateInfo = false" />
    </b-modal>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import UpdateDetails from "./UpdateDetails.vue";

export default {
  components: {
    UpdateDetails
  },
  data() {
    return {
      updateInfo: false
    };
  },
  computed: {
    ...mapGetters(["user"])
  }
};
</script>

<style lang="scss" scoped>
.my-account {
  min-height: 100vh;
}
h1 {
  font-size: 2rem;
  font-weight: 700;
  text-align: center;
}
.flex-align {
  display: flex;
  justify-content: space-between;
}
.flex-center {
  display: flex;
  justify-content: center;
}
h3 {
  font-size: 1.5rem;
}

.order-details {
  display: grid;
  grid-template-columns: 65%;
  justify-content: center;
}

.b-table .table tr.detail {
  background: green !important;
}

h2 {
  font-size: 1.4rem;
  font-weight: 700;
}
h2 span {
  font-size: 1.2rem;
  font-weight: 500;
}
</style>
