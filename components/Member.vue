<template>
  <div class="member">
    <img class="member-img" :src="member.img" :alt="member.imgDesc" />
    <h3 class="member-title">{{ member.name }}</h3>
    <div class="member-desc" v-html="member.desc"></div>
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
.member-img {
  border-radius: 50%;
  border: var(--color-primary) 3px solid;
  text-align: center;
  margin: auto;
}

.member {
  width: 300px;
  min-height: 8em;
  display: flex;
  flex-flow: row wrap;
}

.member-desc {
  text-align: center;
  margin: auto;
}

.member-title {
  text-align: center;
  margin: 16px auto;
}

</style>
