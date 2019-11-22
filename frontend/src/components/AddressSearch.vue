<template>
  <!-- container for places.js -->
  <div />
</template>

<script>
import places from "places.js";

export default {
  data() {
    return { instance: null };
  },
  mounted() {
    // make sure Vue does not know about the input
    // this way it can properly unmount
    this.input = document.createElement("input");
    this.$el.appendChild(this.input);

    this.instance = places({
      apiKey: process.env.ALGOLIA_SEARCH_API_KEY,
      appId: process.env.ALGOLIA_APPLICATION_ID,
      container: this.input
    });

    this.instance.on("change", e => {
      this.$emit("change", e);
    });
  },
  beforeDestroy() {
    this.instance.off("change");
    this.instance.destroy();
  }
};
</script>
