<template>
  <div class="card text-center">
    <div class="card-body">
      <form @submit.prevent="submit">
        <div class="mb-3 row">
          <label class="col-sm-3 col-form-label"># de Placa</label>
          <div class="col-sm-8">
            <input
              type="text"
              class="form-control"
              v-model="form.plate"
              disabled
              readonly
            />
          </div>
        </div>
        <div class="mb-3 row">
          <label for="tdoc" class="col-sm-3 col-form-label"
            >Marca</label
          >
          <div class="col-sm-8">
            <input
              type="text"
              class="form-control"
              v-model="form.brand"
              id="tdoc"
            />
          </div>
        </div>
        <div class="mb-3 row">
          <label for="nombre" class="col-sm-3 col-form-label"
            >Modelo</label
          >
          <div class="col-sm-8">
            <input
              type="text"
              class="form-control"
              v-model="form.model"
              id="nombre"
            />
          </div>
        </div>
        <div class="mb-3 row">
          <label for="direccion" class="col-sm-3 col-form-label"
            >Año</label
          >
          <div class="col-sm-8">
            <input
              type="number"
              class="form-control"
              v-model="form.year"
              id="direccion"
            />
          </div>
        </div>
        <div class="mb-3 row">
          <label for="telefono" class="col-sm-3 col-form-label"
            >Color</label
          >
          <div class="col-sm-8">
            <input
              type="text"
              class="form-control"
              v-model="form.color"
              id="telefono"
            />
          </div>
        </div>
        <div class="mb-3 row">
          <label for="email" class="col-sm-3 col-form-label"
            >Documento del propietario</label
          >
          <div class="col-sm-8">
            <input
              type="text"
              class="form-control"
              v-model="form.owner.id"
              id="email"
            />
          </div>
        </div>
        <div>
          <router-link to="/dashboard/vehicles" class="btn">Atras</router-link>
          <button type="submit" class="btn">Actualizar</button>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue'
import { mapGetters, mapActions } from 'vuex'
export default defineComponent({
  name: 'EditVehicleView',
  data () {
    return {
      form: {
        plate: '',
        brand: '',
        model: '',
        year: '',
        color: '',
        owner: {
          id: ''
        }
      }
    }
  },
  props: ['id'],
  async created () {
    try {
      await this.viewVehicle(this.id)
      this.form.plate = this.vehicle.plate
      this.form.brand = this.vehicle.brand
      this.form.model = this.vehicle.model
      this.form.year = this.vehicle.year
      this.form.color = this.vehicle.color
      this.form.owner.id = this.vehicle.owner.id
    } catch (error) {
      console.error(error)
      this.$router.push('/dashboard/vehicles')
    }
  },
  computed: {
    ...mapGetters({ vehicle: 'setVehicle' })
  },
  methods: {
    ...mapActions(['updateVehicle', 'viewVehicle']),
    async submit () {
      try {
        const vehicle = {
          id: this.id,
          form: this.form
        }
        await this.updateVehicle(vehicle)
        this.$router.push({ name: 'Vehicle', params: { id: this.vehicle.plate } })
      } catch (error) {
        console.log(error)
      }
    }
  }
})
</script>
