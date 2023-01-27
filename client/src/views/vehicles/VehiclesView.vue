<template>
  <div v-if="vehicles?.length">
    <table class="table table-hover text-center">
      <thead>
        <tr>
          <th scope="col"># de Placa</th>
          <th scope="col">Marca</th>
          <th scope="col">Modelo</th>
          <th scope="col">
            <button
              type="button"
              class="btn btn-sm"
              data-bs-toggle="modal"
              data-bs-target="#staticBackdrop"
            >
              Agregar vehiculo
            </button>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="vehicle in vehicles" :key="vehicle.plate">
          <th scope="row">{{ vehicle.plate }}</th>
          <td>{{ vehicle.brand }}</td>
          <td>{{ vehicle.model }}</td>
          <td>
            <div class="d-grid gap-2 d-md-block text-center">
              <router-link
                :to="{ name: 'Vehicle', params: { id: vehicle.plate } }"
                >Ver</router-link
              >
              <router-link
                :to="{ name: 'VehicleEdit', params: { id: vehicle.plate } }"
                >Editar</router-link
              >
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <div v-else>
    <table class="table table-hover text-center">
      <thead>
        <tr>
          <th scope="col"># de Placa</th>
          <th scope="col">Marca</th>
          <th scope="col">Modelo</th>
          <th scope="col">
            <button
              type="button"
              class="btn btn-sm"
              data-bs-toggle="modal"
              data-bs-target="#staticBackdrop"
            >
              Agregar vehiculo
            </button>
          </th>
        </tr>
      </thead>
      <tbody>
      </tbody>
    </table>
  </div>

  <!-- Modal -->
  <div
    class="modal fade"
    id="staticBackdrop"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">
            Nuevo vehiculo
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submit">
            <div class="mb-3 row">
              <label for="id" class="col-sm-4 col-form-label"
                ># de Placa</label
              >
              <div class="col-sm-8">
                <input
                  type="text"
                  class="form-control"
                  v-model="form.plate"
                  id="id"
                />
              </div>
            </div>
            <div class="mb-3 row">
              <label for="tdoc" class="col-sm-4 col-form-label"
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
              <label for="nombre" class="col-sm-4 col-form-label"
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
              <label for="direccion" class="col-sm-4 col-form-label"
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
              <label for="telefono" class="col-sm-4 col-form-label"
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
              <label for="dcopro" class="col-sm-4 col-form-label"
                >Documento Propietario</label
              >
              <div class="col-sm-8">
                <input
                  type="number"
                  class="form-control"
                  v-model="form.owner_id"
                  id="dcopro"
                />
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn" data-bs-dismiss="modal">
                Cancelar
              </button>
              <button type="submit" class="btn" data-bs-dismiss="modal">
                Agregar
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue'
import { mapGetters, mapActions } from 'vuex'
export default defineComponent({
  name: 'VehiclesView',
  data () {
    return {
      form: {
        plate: '',
        brand: '',
        model: '',
        year: '',
        color: '',
        owner_id: ''
      }
    }
  },
  created: function () {
    return this.$store.dispatch('getVehicles')
  },
  computed: {
    ...mapGetters({ vehicles: 'setVehicles' })
  },
  methods: {
    ...mapActions(['createVehicle']),
    async submit () {
      await this.createVehicle(this.form)
      this.form.plate = ''
      this.form.brand = ''
      this.form.model = ''
      this.form.year = ''
      this.form.color = ''
      this.form.owner_id = ''
    }
  }
})
</script>
