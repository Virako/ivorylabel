<template>
  <div class="menu">
    <nav role="off-canvas" class="nav-menu">
      <ul class="menu-list">
        <li class="menu-item">
          <a class="link active" v-scroll-to="'#members'" href="#">
            {{ $t('pages.about.title') }}
          </a>
        </li>
        <li class="menu-item">
          <a class="link" v-scroll-to="'#services'" href="#">
            {{ $t('pages.services.title') }}
          </a>
        </li>
        <li class="menu-item">
          <a class="link" v-scroll-to="'#recording'" href="#">
            {{ $t('pages.recording.title') }}
          </a>
        </li>
        <li class="menu-item">
          <a class="link" v-scroll-to="'#projects'" href="#">
            {{ $t('pages.projects.title') }}
          </a>
        </li>
        <li class="menu-item">
          <a class="link" v-scroll-to="'#contact'" href="#">
            {{ $t('pages.contact.title') }}
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
const VueScrollTo = require('vue-scrollto')

export default Vue.extend({})
Vue.use(VueScrollTo)
</script>

<style>
.menu {
  margin-right: 1em;
}

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
  width: 100%;
}

@media screen and (max-width: 60em) {
  #menu {
    position: relative;
    display: block;
    z-index: -2;
    opacity: 0;
  }

  .nav-menu {
    display: block;
    width: 100%;
    left: 0;
    z-index: 1;
  }

  .menu-item {
    height: 100%;
    width: 100%;
    margin: 0;
    display: table;
  }
}
</style>
