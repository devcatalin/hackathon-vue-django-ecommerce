<template>
  <a :href="redirectLink">{{ text }}</a>
</template>

<script>
export default {
  props: {
    text: String,
    redirectLink: String
  }
};
</script>

<style scoped>
a {
  color: white;
  background-color: #2e7d32;
  height: 2rem;
  padding: 0.15rem 1rem;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.5s;
}

a:hover {
  background-color: #4caf50;
}
</style>
