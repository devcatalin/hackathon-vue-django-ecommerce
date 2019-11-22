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
  background-color: #4caf50;
  height: 3rem;
  padding: 0.5rem 1.5rem;
  margin: 0 auto;
  font-size: 1.3rem;
  transition: all 0.5s cubic-bezier(0.65, -0.25, 0.25, 1.95);
  cursor: pointer;
}

a:hover {
  letter-spacing: 0.15rem;
  color: white;
}
</style>
