<template>
  <nav role="navigation" class="nav-menu">
    <div id="menuToggle">
      <input class="hamburger" type="checkbox" />
      <span></span>
      <span></span>
      <span></span>

      <ul id="menu" class="menu-list">
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
    </div>
  </nav>
</template>

<script lang="ts">
import Vue from 'vue'
const VueScrollTo = require('vue-scrollto')

export default Vue.extend({})
Vue.use(VueScrollTo)
</script>

<style>
.menu-item {
  margin: 0.5em;
  display: inline-flex;
  text-align: center;
}

.menu-item > a:hover {
  font-weight: bold;
  color: var(--color-hover);
}

.hamburger {
  display: none;
}

@media screen and (max-width: 60em) {
  #menuToggle {
    position: relative;
    right: 8px;
    z-index: 1;
    -webkit-user-select: none;
    user-select: none;
  }

  #menuToggle a {
    text-decoration: none;
    color: #232323;
    transition: color 0.3s ease;
  }

  #menuToggle a:hover {
    color: var(--color-hover);
  }

  #menuToggle input {
    display: block;
    width: 40px;
    height: 32px;
    position: absolute;
    top: -7px;
    left: -5px;
    cursor: pointer;
    opacity: 0; /* hide this */
    z-index: 2; /* and place it over the hamburger */
    -webkit-touch-callout: none;
  }

  /*
   * Just a quick hamburger
   */
  #menuToggle span {
    display: block;
    width: 33px;
    height: 4px;
    margin-bottom: 5px;
    position: relative;
    background: var(--color-link);
    border-radius: 3px;
    z-index: 1;
    transform-origin: 4px 0;
    transition: transform 0.5s cubic-bezier(0.77,0.2,0.05,1.0),
                background 0.5s cubic-bezier(0.77,0.2,0.05,1.0),
                opacity 0.55s ease;
  }

  #menuToggle span:first-child {
    transform-origin: 0% 0%;
  }

  #menuToggle span:nth-last-child(2) {
    transform-origin: 0% 100%;
  }

  /*
   * Transform all the slices of hamburger
   * into a crossmark.
   */
  #menuToggle input:checked ~ span {
    opacity: 1;
    transform: rotate(45deg) translate(-2px, -1px);
    background: var(--color-link);
  }

  /*
   * But let's hide the middle one.
   */
  #menuToggle input:checked ~ span:nth-last-child(3) {
    opacity: 0;
    transform: rotate(0deg) scale(0.2, 0.2);
  }

  /*
   * Ohyeah and the last one should go the other direction
   */
  #menuToggle input:checked ~ span:nth-last-child(2) {
    transform: rotate(-45deg) translate(0, -1px);
  }

  /*
   * Make this absolute positioned
   * at the top left of the screen
   */
  #menu {
    position: absolute;
    width: 220px;
    margin: 40px 0 0 -160px;
    padding: 0;
    background: white;
    list-style-type: none;
    -webkit-font-smoothing: antialiased;

    /* to stop flickering of text in safari */
    transform-origin: 0% 0%;
    transform: translate(100%, 0);
    transition: transform 0.5s cubic-bezier(0.77,0.2,0.05,1.0);
  }

  #menu li {
    padding: 8px 0;
  }

  /*
   * And let's slide it in from the left
   */
  #menuToggle input:checked ~ ul {
    transform: none;
  }
}
</style>
