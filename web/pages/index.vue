<template>
  <div>
    <Header :scrollY="scrollY" />

    <div class="container">
      <div class="content">
        <section id="home">
          <div class="home-img"></div>
          <div class="home-title">
            <h2>Ivory Label</h2>
            <span v-html="data.about"></span>
          </div>
        </section>

        <section id="members">
          <h2 class="title">¿Quiénes somos?</h2>
          <div class="members">
            <span v-for="(member, index) in data.members" :key="index">
              <Member :member="member" :index="index" />
            </span>
          </div>
        </section>

        <section id="services">
          <h2 class="title">Servicios</h2>
          <div class="services">
            <span v-for="(service, index) in data.services" :key="index">
              <Service :service="service" :index="index" />
            </span>
          </div>
        </section>

        <section id="recording">
          <h2 class="title">Estudio Online</h2>
          <div class="paragraph" v-html="data.recording"></div>
        </section>

        <section id="projects">
          <h2 class="title">Ivory Project</h2>
          <div class="projects">
            <span v-for="(project, index) in data.projects" :key="index">
              <Project v-bind="project" :index="index" />
            </span>
          </div>
        </section>
      </div>

      <Footer :text="data.contact" />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import content from '@/static/data.json'


export default Vue.extend({
  data() {
    return {
      data: content,
      scrollY: false
    }
  },
  methods: {
    handleScroll() {
      if (window.scrollY > 0) {
        this.scrollY = true
      } else {
        this.scrollY = false
      }
      console.log(this.scrollY, window.scrollY)
    }
  },
  created() {
    if (process.client) {
      window.addEventListener('scroll', this.handleScroll)
    }
  },
  destroyed() {
    if (process.client) {
      window.removeEventListener('scroll', this.handleScroll)
    }
  },
  async asyncData(context) {
    try {
      const data = await context.app.$axios.$get('https://ivorylabel.es/st/static/data.json')
      return { data }
    } catch (e) {
      context.error(e)
    }
  },
})
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
}

.home-img {
  width: 100%;
  background-image: url('~@/assets/images/bg_header.jpg');
  filter: opacity(70%) grayscale(100%);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: 60vh;
}

.home-title {
  position: absolute;
  height: 60vh;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}

.content {
  flex: 1 0 auto;
}

.title {
  padding: 1em 1em;
  background-color: var(--background-light);
  text-align: center;
}

.services,
.members {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  max-width: 1200px;
  margin: auto;
  gap: 32px;
  margin-top: 32px;
}

.paragraph {
  max-width: 80ch;
  margin: auto;
}

@media screen and (max-width: 60em) {
  .paragraph {
    margin: auto 8px;
  }
}
</style>
