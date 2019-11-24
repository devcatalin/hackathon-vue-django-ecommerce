<template>
  <div class="my-account m-t-xl p-lg">
    <user-profile />
    <div class="card orders-card p-lg">
      <h1 class="m-b-lg">Comenzile mele</h1>
      <b-table :data="invoices" ref="table">
        <template slot-scope="props">
          <b-table-column field="id" label="ID" width="40" numeric>
            {{
            props.row.id
            }}
          </b-table-column>

          <b-table-column field="summary" label="Descriere">
            {{
            props.row.summary
            }}
          </b-table-column>

          <b-table-column field="total_cost" label="Cost total" numeric>
            {{
            props.row.total_cost
            }}
          </b-table-column>

          <b-table-column field="total_cost" label="Data si ora" numeric>
            {{
            props.row.date.replace("T", " ").replace("Z", " ").slice(0, -8)
            }}
          </b-table-column>
        </template>
      </b-table>
    </div>
  </div>
</template>

<script>
import http from "@/http";
import UserProfile from "../components/Profile.vue";

export default {
  components: {
    UserProfile
  },
  methodes: {
    toggle(row) {
      this.$refs.table.toggleDetails(row);
    }
  },
  beforeMount() {
    http.get("/api/shop/invoices/list/").then(response => {
      this.invoices = response.data;
    });
  },
  data() {
    return {
      deleteOrder: false,
      defaultOpenedDetails: [],
      showDetailIcon: true,
      invoices: [],
      orderData: [
        {
          name: "Rosii",
          u_m: "KG",
          cantity: 50,
          price: "512 Lei"
        },
        {
          name: "Cartofi",
          u_m: "KG",
          cantity: 102,
          price: "255 Lei"
        }
      ]
    };
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
