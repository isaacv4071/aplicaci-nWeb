<template>
  <div class="card text-center">
    <div class="card-header">Propietario</div>
    <div class="card-body">
      <dl>
        <dt>Numero de Placa</dt>
        <dd>{{ vehicle.plate }}</dd>
        <dt>Marca</dt>
        <dd>{{ vehicle.brand }}</dd>
        <dt>Modelo</dt>
        <dd>{{ vehicle.model }}</dd>
        <dt>Año</dt>
        <dd>{{ vehicle.year }}</dd>
        <dt>Color</dt>
        <dd>{{ vehicle.color }}</dd>
        <dt>Documento Propietario</dt>
        <dd>{{ vehicle.owner.id }}</dd>
      </dl>
    </div>
    <div class="card-footer text-muted text-center">
      <router-link to="/dashboard/vehicles" class="btn">Atras</router-link>
      <button @click="removeNote()" class="btn">Eliminar</button>
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue'
import { mapGetters, mapActions } from 'vuex'

export default defineComponent({
  name: 'VehicleView',
  props: ['id'],
  async created () {
    try {
      await this.viewVehicle(this.id)
    } catch (error) {
      console.error(error)
      this.$router.push('/dashboard/vehicles')
    }
  },
  computed: {
    ...mapGetters({ vehicle: 'setVehicle' })
  },
  methods: {
    ...mapActions(['viewVehicle', 'deleteVehicle']),
    async removeNote () {
      try {
        const text = '¿Desea borrar el propietario?'
        /* eslint-disable */
        if (confirm(text) == true) {
          await this.deleteVehicle(this.id)
          this.$router.push('/dashboard/vehicles')
        } else {
          this.$router.push(`/dashboard/vehicle/${this.id}`)
        }
      } catch (error) {
        console.error(error)
      }
    }
  }
})
</script>