<template>
  <div v-bind:class="{'member':true, 'ligth':(index % 2 != 0)}">
    <div class="member-desc">
      <h3>{{ member.name }}</h3>
      <p>{{ member.desc }}</p>
    </div>
    <div class="member-img">
      <img :src="member.src" alt="desc" />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  props: {
    'member': {
        type: Object,
        default: () => {}
    },
    'index': {
        type: Number,
        default: 0
    }
  }
})
</script>

<style>
/* Default color is dark */
.member {
  background-color: var(--background-dark);
  color: var(--color-light);
  width: 100%;
  min-height: 8em;
  display: flex;
  flex-flow: row wrap;
}

.ligth {
  background-color: var(--background-light);
  color: var(--color-dark);
}

.member-desc {
  flex-grow: 2;
}

.member-img {
  flex-grow: 1;
}

</style>
