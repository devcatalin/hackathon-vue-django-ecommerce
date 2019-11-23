<template>
    <div class="map-view">
        <l-map :zoom="7" :center="[46.023546, 24.8259625]" class="map">
            <l-tile-layer
                url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
            ></l-tile-layer>
            <l-marker
                v-for="location in locations"
                :key="location.title"
                :lat-lng="location.latlong"
            >
                <l-popup>
                    <h2>{{ location.title }}</h2>
                </l-popup>
            </l-marker>
        </l-map>
    </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";
export default {
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LPopup
    },
    data() {
        return {
            locations: [
                { latlong: [46.023546, 24.8259625], title: "Nume firma" }
            ]
        };
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
