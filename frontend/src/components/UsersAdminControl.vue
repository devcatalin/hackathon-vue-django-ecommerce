<template>
  <div class="m-t-md p-lg">
    <b-table :data="userList">
      <template slot-scope="props">
        <b-table-column field="name" label="Nume utlizator">
          {{
          props.row.username
          }}
        </b-table-column>
        <b-table-column field="full_name" label="Nume">
          {{
          props.row.full_name
          }}
        </b-table-column>
        <b-table-column field="phone_number" label="Numar de telefon">
          {{
          props.row.phone_number
          }}
        </b-table-column>
        <b-table-column field="address" label="Adresa">
          {{
          props.row.address
          }}
        </b-table-column>
        <b-table-column field="buyer_type" label="Tip cumpărători">
          {{
          props.row.buyer_type
          }}
        </b-table-column>
        <b-table-column width="50" field="price">
          <a @click="showDeleteModal(props.row.username)">
            <b-icon type="is-danger" icon="delete"></b-icon>
          </a>
        </b-table-column>
      </template>
    </b-table>

    <b-modal :active.sync="userDeleteModal.visibility" has-modal-card :can-cancel="true">
      <div class="card p-md modal-content">
        <h3 class="m-b-lg">Sunteți siguri că doriți să ștergeți acest utilizator?</h3>
        <div class="flex-align">
          <b-button type="is-primary" @click="closeDeleteModal">Anulează</b-button>
          <b-button type="is-danger" @click="deleteUser">Confirmă</b-button>
        </div>
      </div>
    </b-modal>

    <h2 class="m-t-xl level-right">Număr de utilizatori: {{ userList.length }}</h2>
  </div>
</template>

<script>
import http from "@/http";

export default {
  data() {
    return {
      userDeleteModal: {
        visibility: false,
        userToDelete: null
      },
      userList: []
    };
  },
  beforeMount() {
    this.fetchUserList();
  },
  methods: {
    fetchUserList() {
      http.get("/api/users/user-list/").then(response => {
        this.userList = response.data;
      });
    },
    showDeleteModal(username) {
      this.userDeleteModal = {
        visibility: true,
        userToDelete: username
      };
    },
    closeDeleteModal() {
      this.userDeleteModal = {
        visibility: false,
        userToDelete: null
      };
    },
    deleteUser() {
      http
        .post("/api/users/user-delete/", {
          username: this.userDeleteModal.userToDelete
        })
        .then(() => {
          this.fetchUserList();
          this.$buefy.toast.open("Utilizatorul a fost șters cu succes.");
          this.closeDeleteModal();
        });
    }
  }
};
</script>

<style lang="scss" scoped>
h2 {
  font-size: 1.5rem;
  font-weight: 600;
}
h3 {
  font-size: 1.3rem;
}
</style>
