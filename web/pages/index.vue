<template>
  <div>
    <Header />

    <div class="container">
      <div class="content">
        <section id="members">
          <h2 class="title">¿Quiénes somos?</h2>
          <div class="paragraph" v-html="data.about"></div>
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

        <section id="contact">
          <h2 class="title">Contacto</h2>
          <div class="paragraph" v-html="data.contact"></div>
        </section>
      </div>
      <Footer />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import content from '@/static/data.json'

const DOMAIN = process.env.BASE_URL || 'http://172.23.0.4'

export default Vue.extend({
  data() {
    return {
      "data": content
    }
  },
  async fetch() {
    this.data = await fetch(
       DOMAIN + '/st/static/data.json'
    ).then(
      res => res.json()
    ).catch(
      err => {}
    )
  },
})
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
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
