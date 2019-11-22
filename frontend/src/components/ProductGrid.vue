<template>
  <div class="card product-grid-card">
    <img src="https://via.placeholder.com/1000x700" alt="Placeholder image" />
    <div class="card-content">
      <h2 class="m-b-sm">{{title}}</h2>
      <p>{{price}} Lei</p>
    </div>
    <a href="#">
      <b-icon class="m-r-sm" icon="square-inc-cash" size="is-small"></b-icon>Cumpara acum
    </a>
  </div>
</template>

<script>
export default {
  props: {
    price: Number,
    title: String
  }
};
</script>

<style lang="scss" scoped>
.product-grid-card {
  height: 22rem;
  width: 16rem;

  display: grid;
  grid-template-rows: max-content 1fr 2rem;
  align-items: center;
}

h2 {
  font-size: 1.5rem;
  font-weight: 500;
  text-align: center;
  margin-bottom: 1rem;
}

p {
  text-align: center;
}

a {
  text-align: center;
  background-color: #2e7d32;
  color: white;
  padding: 0.5rem;
  transition: all 0.5s;
}

a:hover {
  background-color: #4caf50;
}
</style>