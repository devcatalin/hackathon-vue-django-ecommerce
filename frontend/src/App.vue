<template>
  <div id="app">
    <b-loading :is-full-page="true" :active.sync="isLoading"></b-loading>
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import { mapGetters } from "vuex";

export default {
  components: { Navbar },
  computed: {
    ...mapGetters(["isLoading", "isAuthenticated", "user"])
  },
  beforeMount() {
    this.$store.dispatch("fetchCategories");
    this.$store.dispatch("fetchSellers");
    this.$store.dispatch("getCart");
    if (this.isAuthenticated) {
      this.$store.dispatch("fetchUserData");
    }
  }
};
</script>

<style lang="scss">
body {
  background-color: #eeeeee;
  min-height: 100vh;
}

.flex-align {
  display: flex;
  justify-content: space-between;
}

.flex-center {
  display: flex;
  justify-content: center;
}

*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: inherit;
}

#app {
  font-family: "Tajawal", sans-serif !important;
}

html {
  box-sizing: border-box;
  font-size: 62.5%; /* 1rem = 10px */
}

a {
  text-decoration: none;
}

@media only screen and (max-width: 950px) {
  html {
    font-size: 85% !important;
  }
}
@media only screen and (min-width: 1700px) {
  html {
    font-size: 125% !important;
  }
}

// Import Bulma's core
@import "~bulma/sass/utilities/_all";

// Set your colors
$primary: #4caf50;
$primary-invert: findColorInvert($primary);
$twitter: #4099ff;
$twitter-invert: findColorInvert($twitter);

// Setup $colors to use as bulma classes (e.g. 'is-twitter')
$colors: (
  "white": (
    $white,
    $black
  ),
  "black": (
    $black,
    $white
  ),
  "light": (
    $light,
    $light-invert
  ),
  "dark": (
    $dark,
    $dark-invert
  ),
  "primary": (
    $primary,
    $primary-invert
  ),
  "info": (
    $info,
    $info-invert
  ),
  "success": (
    $success,
    $success-invert
  ),
  "warning": (
    $warning,
    $warning-invert
  ),
  "danger": (
    $danger,
    $danger-invert
  ),
  "twitter": (
    $twitter,
    $twitter-invert
  )
);

// Links
$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";

$sizeUnit: rem;
$marginKey: "m";
$paddingKey: "p";
$separator: "-";
$sizes: (
  ("none", 0),
  ("xxs", 0.125),
  ("xs", 0.25),
  ("sm", 0.5),
  ("md", 1),
  ("lg", 2),
  ("xl", 4),
  ("xxl", 8)
);
$positions: (("t", "top"), ("r", "right"), ("b", "bottom"), ("l", "left"));

@function sizeValue($key, $value) {
  @return if($key == "none", 0, $value + $sizeUnit);
}

@each $size in $sizes {
  $sizeKey: nth($size, 1);
  $sizeValue: nth($size, 2);
  .#{$marginKey}#{$separator}#{$sizeKey} {
    margin: sizeValue($sizeKey, $sizeValue);
  }
  .#{$paddingKey}#{$separator}#{$sizeKey} {
    padding: sizeValue($sizeKey, $sizeValue);
  }
  @each $position in $positions {
    $posKey: nth($position, 1);
    $posValue: nth($position, 2);
    .#{$marginKey}#{$separator}#{$posKey}#{$separator}#{$sizeKey} {
      margin-#{$posValue}: sizeValue($sizeKey, $sizeValue);
    }
    .#{$paddingKey}#{$separator}#{$posKey}#{$separator}#{$sizeKey} {
      padding-#{$posValue}: sizeValue($sizeKey, $sizeValue);
    }
  }
}
</style>
