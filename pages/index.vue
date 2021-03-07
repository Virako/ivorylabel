<template>
  <div>
    <Header />

    <div class="container">
      <div class="content">

        <section id="members">
          <h2 class="title">¿Quiénes somos?</h2>
          <div class="paragraph" v-html="about"></div>
          <div class="members">
            <span v-for="(member, index) in members" v-bind:key="index">
              <Member v-bind:member="member" v-bind:index="index" />
            </span>
          </div>
        </section>

        <section id="services">
          <h2 class="title">Servicios</h2>
          <div class="services">
            <span v-for="(service, index) in services" v-bind:key="index">
              <Service v-bind:service="service" v-bind:index="index" />
            </span>
          </div>
        </section>

        <section id="recording">
          <h2 class="title">Estudio Online</h2>
          <div class="paragraph" v-html="recording"></div>
        </section>

        <section id="projects">
          <h2 class="title">Ivory Project</h2>
          <h3 class="title">Ivory Live</h3>
          <div class="services">
            <span v-for="(service, index) in services" v-bind:key="index">
              <Service v-bind:service="service" v-bind:index="index" />
            </span>
          </div>
          <h3 class="title">Ivory Session</h3>
          <div class="services">
            <span v-for="(service, index) in services" v-bind:key="index">
              <Service v-bind:service="service" v-bind:index="index" />
            </span>
          </div>
        </section>

        <section id="contact">
          <h2 class="title">Contacto</h2>
          <div class="paragraph" v-html="about"></div>
        </section>

      </div>
      <Footer />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import content from '@/static/data.json'

export default Vue.extend({
  data() {
    return content

  }
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

.services, .members {
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
