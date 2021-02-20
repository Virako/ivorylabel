<template>
  <div class="menu">
    <label for="menu" onclick></label>
    <input type="checkbox" id="menu" alt="active this check for show menu">
    <nav role="off-canvas" class="nav-menu">
      <ul class="menu-list">
        <li class="menu-item">
          <nuxt-link :to="localeRoute('/')">
            {{ $t('pages.home.title') }}
          </nuxt-link>
        </li>
        <li class="menu-item">
          <nuxt-link :to="localeRoute('/que-hacemos')">
            {{ $t('pages.what.title') }}
          </nuxt-link>
        </li>
        <li class="menu-item">
          <nuxt-link :to="localeRoute('/proyectos')">
            {{ $t('pages.projects.title') }}
          </nuxt-link>
        </li>
        <li class="menu-item">
          <nuxt-link :to="localeRoute('/tienda')">
            {{ $t('pages.store.title') }}
          </nuxt-link>
        </li>
        <li class="menu-item">
          <nuxt-link :to="localeRoute('/quienes-somos')">
            {{ $t('pages.about.title') }}
          </nuxt-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({})
</script>

<style>

.menu {
  margin-right: 1em;
}

#menu {
  display: none;
}

.menu-list {
  padding: 0;
}

.menu-item {
  margin: .5em;
  display: inline-flex;
  text-align: center;
}

.menu-item > a:hover, .menu-item > a:focus {
  font-weight: bold;
}

@media screen and (max-width: 60em) {
  #menu {
    position: relative;
    display: block;
    z-index: -2;
    opacity: 0;
  }

  .nav-menu {
    display: none;
  }

  .menu-item {
    height: 100%;
    width: 100%;
    margin: 0;
    display: table;
  }

  label {
    display: block;
    position: absolute;
    top: 3em;
    right: 1em;
    width: 2em;
    height: 2em;
    padding: 0;
    font-size: 1.1em;
    cursor: pointer;
    margin: 0;
    border: 1px solid var(--color-primary);
    border-radius: 5px;
  }

  label::after {
    position: absolute;
    left: 0.2em;
    top: -0.2em;
    content: "\2261";
    font-size: 2em;
    color: var(--color-primary);
  }

  label:hover {
    border: 2px solid var(--color-primary);
  }

  #menu:focus + label {
    border: 2px solid var(--color-primary);
  }

  #menu:checked ~ .nav-menu {
    display: block;
    position: absolute;
    padding-top: 4em;
    padding-bottom: 1em;
    width: 100%;
    left: 0;
    background-color: var(--background-menu);
    z-index: -1;
  }

  #menu:checked ~ .menu-item {
    padding: .55em .55em .55em 1.5em;
  }

  #menu:checked {
    z-index: -1;
  }

}
</style>
