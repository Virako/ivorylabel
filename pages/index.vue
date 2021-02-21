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

export default Vue.extend({
  data() {
    return {
      members: [
        {
          'name': 'David Ramírez de la Corte',
          'desc': 'Doo amatomaa va usté muy cargadoo te va a hasé pupitaa te va a hasé pupitaa la caidita. Benemeritaar pecador',
          'img': 'https://picsum.photos/200/200'
        },
        {
          'name': 'Víctor Ramírez de la Corte',
          'desc': 'Poca cosa, algo cortito',
          'img': 'https://picsum.photos/200/200'
        },
        {
          'name': 'Alex Villanueva',
          'desc': 'Emprendedor desde el inicio de su carrera, trabaja en todo tipo de vertientes, haciéndolo un todo terreno en el mundo creativo, beatmaking, producción, 3D... captura con entusiasmo la idea global del producto para que sea única. Tan pronto hace que te veas en tres dimensiones, como te hace un arreglo de pianos y syntes que ya le gustaría a john willians.',
          'img': 'https://picsum.photos/200/200'
        }
      ],
      about: 'Lorem fistrum tiene musho peligro pecador llevame al sircoo al ataquerl no te digo trigo por no llamarte Rodrigor fistro hasestá la cosa muy malar caballo blanco caballo negroorl ese que llega se calle ustée. Amatomaa papaar papaar la caidita de la pradera ese hombree la caidita ese hombree.',
      recording: 'Lorem fistrum tiene musho peligro pecador llevame al sircoo al ataquerl no te digo trigo por no llamarte Rodrigor fistro hasta luego Lucas a peich sexuarl pecador. Benemeritaar a peich no puedor se calle ustée se calle ustée de la pradera condemor pecador caballo blanco caballo negroorl benemeritaar quietooor. Tiene musho peligro tiene musho peligro te va a hasé pupitaa quietooor fistro ese pedazo de. A wan va usté muy cargadoo caballo blanco caballo negroorl torpedo. Pecador apetecan al ataquerl hasta luego Lucas ese que llega pupita a gramenawer. Está la cosa muy malar jarl ahorarr torpedo mamaar está la cosa muy malar no te digo trigo por no llamarte Rodrigor te va a hasé pupitaa apetecan te voy a borrar el cerito. Pecador mamaar pupita te va a hasé pupitaa se calle ustée caballo blanco caballo negroorl jarl de la pradera.<br/>Va usté muy cargadoo amatomaa va usté muy cargadoo te va a hasé pupitaa te va a hasé pupitaa la caidita. Benemeritaar pecador pupita por la gloria de mi madre fistro. Hasta luego Lucas caballo blanco caballo negroorl está la cosa muy malar no puedor pecador hasta luego Lucas diodeno. Torpedo a peich diodenoo apetecan llevame al sircoo torpedo. Tiene musho peligro diodeno la caidita caballo blanco caballo negroorl benemeritaar caballo blanco caballo negroorl la caidita llevame al sircoo qué dise usteer pupita me cago en tus muelas. Sexuarl amatomaa hasta luego Lucas mamaar. Por la gloria de mi madre pecador fistro de la pradera a wan apetecan sexuarl está la cosa muy malar caballo blanco caballo negroorl ese que llega se calle ustée. Amatomaa papaar papaar la caidita de la pradera ese hombree la caidita ese hombree.',
      services: [
        {
          'icon': 'microphone-alt',
          'name': 'Grabación',
          'desc': 'usté muy cargadoo te va a hasé pupitaa te va a hasé pupitaa la caidita.'
        },
        {
          'icon': 'cube',
          'name': '3D',
          'desc': 'usté muy cargadoo te va a hasé pupitaa te va a hasé pupitaa la caidita.'
        },
        {
          'icon': 'object-group',
          'name': 'diseño',
          'desc': 'Elegimos y estudiamos cuidadosamente todos los elementos en concordancia con la identidad visual corporativa.  Nuestro objetivo principal es  hacer que te diferencies de la competencia. Nos encantan los retos de crear para transmitir emociones.'
        },
        {
          'icon': 'sliders-h',
          'iconRotate': '90',
          'name': 'Mezcla',
          'desc': 'usté muy cargadoo te va a hasé pupitaa te va a hasé pupitaa la caidita.'
        },
        {
          'icon': 'align-right',
          'iconRotate': '90',
          'name': 'Mastering',
          'desc': 'usté muy cargadoo te va a hasé pupitaa te va a hasé pupitaa la caidita.'
        },
        {
          'icon': 'users-cog',
          'name': 'Arreglos y produccion',
          'desc': 'usté muy cargadoo te va a hasé pupitaa te va a hasé pupitaa la caidita.'
        },
        {
          'icon': 'film',
          'name': 'Videoclip',
          'desc': 'usté muy cargadoo te va a hasé pupitaa te va a hasé pupitaa la caidita.'
        },
        {
          'icon': 'camera-retro',
          'name': 'Fotografía',
          'desc': 'usté muy cargadoo te va a hasé pupitaa te va a hasé pupitaa la caidita. Benemeritaar pecador pupita por la gloria de mi madre fistro. Hasta luego Lucas caballo blanco caballo'
        },
      ]

    }
  }
})
</script>

<style>
.container {
  display: flex;
  flex-direction: column;

  /*
  height: calc(100vh - var(--height-header));
  */

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
}

</style>
