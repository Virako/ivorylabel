<template>
  <nav role="off-canvas" class="nav-menu">
    <ul class="menu-list">
      <li class="menu-item">
        <a class="link" v-scroll-to="'#home'" href="#">
          Inicio
        </a>
      </li>
      <li class="menu-item">
        <a class="link" v-scroll-to="'#members'" href="#">
          ¿Quiénes somos?
        </a>
      </li>
      <li class="menu-item">
        <a class="link" v-scroll-to="'#services'" href="#">
          Servicios
        </a>
      </li>
      <li class="menu-item">
        <a class="link" v-scroll-to="'#recording'" href="#">
          Estudio Online
        </a>
      </li>
      <li class="menu-item">
        <a class="link" v-scroll-to="'#projects'" href="#">
          Ivory Live
        </a>
      </li>
    </ul>
  </nav>
</template>

<script lang="ts">
import Vue from 'vue'
const VueScrollTo = require('vue-scrollto')

export default Vue.extend({})
Vue.use(VueScrollTo)
</script>

<style>
.menu-list {
  padding: 0;
}

.menu-item {
  margin: 0.5em;
  display: inline-flex;
  text-align: center;
}

.menu-item > a.active {
  font-weight: bold;
}

.menu-item > a:hover {
  font-weight: bold;
  color: var(--color-hover);
}

.nav-menu {
 width: auto;

 /* width: 100%; */
}

@media screen and (max-width: 60em) {
  .nav-menu {
    z-index: 1;
  }

  .menu-item {
    height: 100%;
    margin: 0;
    display: table;
  }
}
</style>
