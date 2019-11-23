<template>
    <div class="product-create">
        <form v-on:submit.prevent class="card p-lg">
            <b-field label="Titlu">
                <b-input type="text" v-model="title"></b-input>
            </b-field>
            <b-field>
                <b-upload v-model="thumbnail">
                    <a class="button is-primary">
                        <b-icon icon="upload"></b-icon>
                        <span>Adăugare poză</span>
                    </a>
                </b-upload>
                <span class="file-name" v-if="thumbnail">{{
                    thumbnail.name
                }}</span>
            </b-field>
            <b-field label="Descriere">
                <b-input type="textarea" v-model="description"></b-input>
            </b-field>
            <div class="flex-align">
                <b-field>
                    <b-select placeholder="Selectați o categorie" required>
                        <option value="legume">Legume</option>
                        <option value="fructe">Fructe</option>
                    </b-select>
                </b-field>
                <b-field>
                    <b-select placeholder="Selectați o subcategorie" required>
                        <option value="rosii">Rosii</option>
                        <option value="cartofi">Cartofi</option>
                    </b-select>
                </b-field>
            </div>

            <b-field label="Unitate de măsura">
                <div class="block">
                    <b-radio
                        v-model="quantity_type"
                        name="quantityType"
                        native-value="Kilograme"
                        >Kilogram</b-radio
                    >
                    <b-radio
                        v-model="quantity_type"
                        name="quantityType"
                        native-value="Bucati"
                        >Bucata</b-radio
                    >
                </div>
            </b-field>
            <div class="flex-align">
                <b-field label="Cantitate">
                    <b-input min="0" type="number" v-model="price"></b-input>
                </b-field>
                <b-field label="Preț pe unitate">
                    <b-input type="number" v-model="price"></b-input>
                </b-field>
            </div>

            <button class="button is-primary" type="submit">Salveaza</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            title: "",
            price: "",
            description: "",
            thumbnail: "",
            quantity_type: ""
        };
    }
};
</script>

<style lang="scss" scoped>
.product-create {
    display: grid;
    grid-template-rows: repeat(2, min-content);
    grid-gap: 3rem;
    justify-items: center;
    align-content: center;

    height: 96vh;
}

form {
    display: grid;
    grid-template-columns: 25rem;
    grid-gap: 1rem;
}
</style>
