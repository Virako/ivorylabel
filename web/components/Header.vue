<template>
  <header :class="{ header: true, scroll: scrollY}">
    <nuxt-link class="logo" :to="localeRoute('/')">
      <img class="logo-img" src="@/assets/images/logo.svg" alt="logo" />
    </nuxt-link>
    <Menu />
  </header>
</template>

<script lang="ts">
import Vue from 'vue'


export default Vue.extend({
  props: {
    scrollY: {
      type: Boolean,
      default: false,
    },
  },
})
</script>

<style>
.header {
  position: fixed;
  z-index: 2;
  width: 100%;
  top: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 32px;

  @media screen and (max-width: 1200px) {
    padding: 8px 8px;
  }

}

.scroll {
  transition: background-color 0.5s ease;
  background-color: white;
  box-shadow: 0 0 .5em rgba(0, 0, 0, .5);
}

/*
.header :overflow {
  background-color: white;
}
*/

.logo-img {
  width: 300px;
}
</style>
