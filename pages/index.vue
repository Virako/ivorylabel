<template>
  <div>
    <Header />
    <div class="container">
      <div class="content">
        <h2 class="title">Ivory Label</h2>
        <p>
          Lorem fistrum tiene musho peligro pecador llevame al sircoo al ataquerl no te digo trigo por no llamarte Rodrigor fistro hasta luego Lucas a peich sexuarl pecador. Benemeritaar a peich no puedor se calle ustée se calle ustée de la pradera condemor pecador caballo blanco caballo negroorl benemeritaar quietooor. Tiene musho peligro tiene musho peligro te va a hasé pupitaa quietooor fistro ese pedazo de. A wan va usté muy cargadoo caballo blanco caballo negroorl torpedo. Pecador apetecan al ataquerl hasta luego Lucas ese que llega pupita a gramenawer. Está la cosa muy malar jarl ahorarr torpedo mamaar está la cosa muy malar no te digo trigo por no llamarte Rodrigor te va a hasé pupitaa apetecan te voy a borrar el cerito. Pecador mamaar pupita te va a hasé pupitaa se calle ustée caballo blanco caballo negroorl jarl de la pradera.
        </p><br/>
        <p>
Va usté muy cargadoo amatomaa va usté muy cargadoo te va a hasé pupitaa te va a hasé pupitaa la caidita. Benemeritaar pecador pupita por la gloria de mi madre fistro. Hasta luego Lucas caballo blanco caballo negroorl está la cosa muy malar no puedor pecador hasta luego Lucas diodeno. Torpedo a peich diodenoo apetecan llevame al sircoo torpedo. Tiene musho peligro diodeno la caidita caballo blanco caballo negroorl benemeritaar caballo blanco caballo negroorl la caidita llevame al sircoo qué dise usteer pupita me cago en tus muelas. Sexuarl amatomaa hasta luego Lucas mamaar. Por la gloria de mi madre pecador fistro de la pradera a wan apetecan sexuarl está la cosa muy malar caballo blanco caballo negroorl ese que llega se calle ustée. Amatomaa papaar papaar la caidita de la pradera ese hombree la caidita ese hombree.
        </p>
        <h2 class="title">¿Quiénes somos?</h2>
        <div v-for="(member, index) in members" v-bind:key="index">
          <Member v-bind:member="member" v-bind:index="index" />
        </div>
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
          'img': 'png'
        },
        {
          'name': 'Víctor Ramírez de la Corte',
          'desc': 'Poca cosa, algo cortito',
          'img': 'svg'
        },
        {
          'name': 'Otro sin nombre',
          'desc': 'usté muy cargadoo te va a hasé pupitaa te va a hasé pupitaa la caidita. Benemeritaar pecador pupita por la gloria de mi madre fistro. Hasta luego Lucas caballo blanco caballo',
          'img': 'jpeg'
        }
      ]
    }
  }
})
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  height: calc(100vh - var(--height-header));
}
.content {
  flex: 1 0 auto;
}

.title {
  padding: 1em 1em;
  background-color: var(--background-light);
}

</style>
