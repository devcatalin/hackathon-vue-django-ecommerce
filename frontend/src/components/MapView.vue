<template>
  <div class="map-view">
    <l-map :zoom="7" :center="[46.023546, 24.8259625]" class="map">
      <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
      <l-marker
        v-for="seller in sellers"
        :key="seller.username"
        :lat-lng="[seller.longitude, seller.latitude]"
      >
        <l-popup>
          <h2>{{ seller.full_name }}</h2>
        </l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";
export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup
  },
  computed: {
    ...mapGetters(["sellers"])
  }
};
</script>
<style scoped>
.map-view {
  height: 80%;
  width: 95%;
  z-index: 10 !important;
}
h2 {
  font-size: 1rem;
  font-weight: 500;
}

.vue2leaflet-map {
  z-index: 1;
}
</style>
