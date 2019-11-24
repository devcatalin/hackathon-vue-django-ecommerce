<template>
    <div class="register">
        <b-tabs type="is-boxed" :expanded="true">
            <b-tab-item>
                <template slot="header">
                    <b-icon icon="cart-plus"></b-icon>
                    <span>Cumpărător</span>
                </template>
                <register-form
                    buyerTypeLabel="Ce tip de cumpărător ești ?"
                    fullNameLabel="Nume și prenume"
                    user_type="buyer"
                />
            </b-tab-item>
            <b-tab-item>
                <template slot="header">
                    <b-icon icon="account"></b-icon>
                    <span>Vânzător</span>
                </template>
                <register-form
                    buyerTypeLabel="Ce tip de cumpărători vrei să ai ?"
                    fullNameLabel="Denumire companie"
                    user_type="seller"
                />
            </b-tab-item>
        </b-tabs>
    </div>
</template>

<script>
import RegisterForm from "../components/RegisterForm.vue";

export default {
    components: { RegisterForm }
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
