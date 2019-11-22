<template>
  <div class="card product-list-card">
    <img src="https://via.placeholder.com/500" alt />
    <div class="product-list-details">
      <h1>Title</h1>
      <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Deserunt deleniti maxime ipsam magnam, facilis corporis! Ullam eius minima mollitia nihil? Quis, similique porro aut nesciunt repellendus necessitatibus quia reiciendis tempore.</p>
      <div class="product-list-details-bottom">
        <span>238,59 Lei</span>
        <!-- <a href="#">Cumpara acum</a> -->
        <b-button icon-left="cart" type="is-primary">Adauga in cos</b-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.product-list-card {
  width: 95%;
  height: 12rem;

  display: grid;
  grid-template-columns: 12rem 1fr;
  grid-column-gap: 1rem;
}

.product-list-details {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  padding: 0.7rem;

  &-bottom {
    display: flex;
    justify-content: space-between;
  }
}

h1,
p {
  text-align: center;
}

span {
  font-size: 1.3rem;
}

h1 {
  font-size: 1.8rem;
}
</style>