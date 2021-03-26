<template>
  <div class="project">
    <h3 class="title">{{ title }}</h3>
    <div class="carousel-parent">
      <div class="carousel">
        <iframe
          v-for="(slide, index) in slides"
          class="slide"
          :key="index"
          :src="slide"
          width="300"
          height="168"
          loading="lazy"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        >
        </iframe>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  props: {
    title: {
      type: String,
      default: '',
    },
    slides: {
      type: Array,
      default: () => [],
    },
    index: {
      type: Number,
      default: 0,
    },
  },
})
</script>

<style>
.carousel-parent {
  display: flex;
  justify-content: center;
}

.carousel {
  max-width: 1200px;
  margin: auto;
  height: 188px;
  display: flex;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  scrollbar-color: var(--color-hover) white;
}

.slide {
  padding: 0 10px;
}
</style>
