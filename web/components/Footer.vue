<template>
  <footer class="footer">
    <div class="menu-rrss">
      <a class="rrss" href="https://www.instagram.com/ivorylabel00/">
        <font-awesome-layers class="icon fa-3x">
          <font-awesome-icon :icon="['fab', 'instagram']" />
        </font-awesome-layers>
      </a>
      <!--a class="rrss" href="#">
        <font-awesome-layers class="icon fa-3x">
          <font-awesome-icon :icon="['fab', 'youtube']" />
        </font-awesome-layers>
      </a-->
      <a class="rrss" href="https://wa.me/+34685378731">
        <font-awesome-layers class="icon fa-3x">
          <font-awesome-icon :icon="['fab', 'whatsapp']" />
        </font-awesome-layers>
      </a>
      <a class="rrss" href="mailto:contacto@ivorylabel.es">
        <font-awesome-layers class="icon fa-3x">
          <font-awesome-icon :icon="['fas', 'envelope']" />
        </font-awesome-layers>
      </a>
    </div>
    <div class="paragraph footer-text" v-html="text"></div>
  </footer>
</template>

<script lang="ts">
import Vue from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { faEnvelope } from '@fortawesome/free-solid-svg-icons'

Vue.component('font-awesome-icon', FontAwesomeIcon)

library.add(fab, faEnvelope)
export default Vue.extend({
  props: {
    text: {
      type: String,
      default: ""
    },
  },
})
</script>

<style>
.footer {
  margin-top: 8em;
  text-align: center;
  height: var(--height-footer);
  background-color: var(--background-dark);
  display: flex;
  justify-content: space-around;
  flex-direction: column;
}

.menu-rrss {
  display: flex;
  justify-content: center;
  align-content: center;
  padding: 16px;
}

.rrss {
  width: 80px;
}

.footer-text {
  color: white;
}

.footer-text > p {
  color: white;
}
</style>
