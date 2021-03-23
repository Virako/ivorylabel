<template>
  <div class="service">
    <font-awesome-layers class="icon fa-7x">
      <font-awesome-icon
        :icon="service.icon"
        :transform="service.iconRotate ? 'rotate-' + service.iconRotate : ''"
      />
    </font-awesome-layers>
    <h3 class="service-name">{{ service.name }}</h3>
    <div class="service-desc" v-html="service.desc"></div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import {
  FontAwesomeIcon,
  FontAwesomeLayers,
  FontAwesomeLayersText,
} from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component('font-awesome-layers', FontAwesomeLayers)
Vue.component('font-awesome-layers-text', FontAwesomeLayersText)

library.add(fas)

export default Vue.extend({
  props: {
    service: {
      type: Object,
      default: () => {},
    },
    index: {
      type: Number,
      default: 0,
    },
  },
})
</script>

<style>
.service {
  width: 268px;
  min-height: 8em;
  display: flex;
  flex-flow: row wrap;
}

.service-desc {
  text-align: center;
  margin: auto;
}

.service-name {
  text-align: center;
  margin: 16px auto;
}

.icon {
  width: 100%;
  text-align: center;
  color: var(--color-icon);
}
</style>
