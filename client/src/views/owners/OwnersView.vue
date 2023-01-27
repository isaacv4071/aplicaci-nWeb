<template>
  <div v-if="owners?.length">
    <table class="table table-hover text-center">
      <thead>
        <tr>
          <th scope="col">Documento</th>
          <th scope="col">Tipo de Doc.</th>
          <th scope="col">Nombre Completo</th>
          <th scope="col">
            <button
              type="button"
              class="btn btn-sm"
              data-bs-toggle="modal"
              data-bs-target="#staticBackdrop"
            >
              Agregar Propietario
            </button>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="owner in owners" :key="owner.id">
          <th scope="row">{{ owner.id }}</th>
          <td>{{ owner.document_type }}</td>
          <td>{{ owner.full_name }}</td>
          <td>
            <div class="d-grid gap-2 d-md-block text-center">
              <router-link :to="{ name: 'Owner', params: { id: owner.id } }"
                >Ver</router-link
              >
              <router-link :to="{ name: 'OwnerEdit', params: { id: owner.id } }"
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
          <th scope="col">Documento</th>
          <th scope="col">Tipo de Doc.</th>
          <th scope="col">Nombre Completo</th>
          <th scope="col">
            <button
              type="button"
              class="btn btn-sm"
              data-bs-toggle="modal"
              data-bs-target="#staticBackdrop"
            >
              Agregar Propietario
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
            Nuevo Propietario
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
                ># de Identificación</label
              >
              <div class="col-sm-8">
                <input
                  type="number"
                  class="form-control"
                  v-model="form.id"
                  id="id"
                />
              </div>
            </div>
            <div class="mb-3 row">
              <label for="tdoc" class="col-sm-4 col-form-label"
                >Tipo de Documento</label
              >
              <div class="col-sm-8">
                <input
                  type="text"
                  class="form-control"
                  v-model="form.document_type"
                  id="tdoc"
                />
              </div>
            </div>
            <div class="mb-3 row">
              <label for="nombre" class="col-sm-4 col-form-label"
                >Nombre completo</label
              >
              <div class="col-sm-8">
                <input
                  type="text"
                  class="form-control"
                  v-model="form.full_name"
                  id="nombre"
                />
              </div>
            </div>
            <div class="mb-3 row">
              <label for="direccion" class="col-sm-4 col-form-label"
                >Dirección de residencia</label
              >
              <div class="col-sm-8">
                <input
                  type="text"
                  class="form-control"
                  v-model="form.address"
                  id="direccion"
                />
              </div>
            </div>
            <div class="mb-3 row">
              <label for="telefono" class="col-sm-4 col-form-label"
                ># de Telefono</label
              >
              <div class="col-sm-8">
                <input
                  type="number"
                  class="form-control"
                  v-model="form.phone"
                  id="telefono"
                />
              </div>
            </div>
            <div class="mb-3 row">
              <label for="email" class="col-sm-4 col-form-label"
                >Correo electronico</label
              >
              <div class="col-sm-8">
                <input
                  type="email"
                  class="form-control"
                  v-model="form.email"
                  id="email"
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
  name: 'OwnersView',
  data () {
    return {
      form: {
        id: '',
        document_type: '',
        full_name: '',
        address: '',
        phone: '',
        email: ''
      }
    }
  },
  created: function () {
    return this.$store.dispatch('getOwners')
  },
  computed: {
    ...mapGetters({ owners: 'setOwners' })
  },
  methods: {
    ...mapActions(['createOwner']),
    async submit () {
      await this.createOwner(this.form)
      this.form.id = ''
      this.form.document_type = ''
      this.form.full_name = ''
      this.form.address = ''
      this.form.phone = ''
      this.form.email = ''
    }
  }
})
</script>
