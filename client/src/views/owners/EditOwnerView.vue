<template>
  <div class="card text-center">
    <div class="card-body">
      <form @submit.prevent="submit">
        <div class="mb-3 row">
          <label class="col-sm-3 col-form-label"># de Identificación</label>
          <div class="col-sm-8">
            <input
              type="number"
              class="form-control"
              v-model="owner.id"
              disabled
              readonly
            />
          </div>
        </div>
        <div class="mb-3 row">
          <label for="tdoc" class="col-sm-3 col-form-label"
            >Tipo de Documento</label
          >
          <div class="col-sm-8">
            <input
              type="text"
              class="form-control"
              v-model="form.document_type"
              id="tdoc"
              disabled
              readonly
            />
          </div>
        </div>
        <div class="mb-3 row">
          <label for="nombre" class="col-sm-3 col-form-label"
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
          <label for="direccion" class="col-sm-3 col-form-label"
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
          <label for="telefono" class="col-sm-3 col-form-label"
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
          <label for="email" class="col-sm-3 col-form-label"
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
        <div>
          <router-link to="/dashboard/owners" class="btn">Atras</router-link>
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
  name: 'OwnerView',
  data () {
    return {
      form: {
        document_type: '',
        full_name: '',
        address: '',
        phone: '',
        email: ''
      }
    }
  },
  props: ['id'],
  async created () {
    try {
      await this.viewOwner(this.id)
      this.form.document_type = this.owner.document_type
      this.form.full_name = this.owner.full_name
      this.form.address = this.owner.address
      this.form.phone = this.owner.phone
      this.form.email = this.owner.email
    } catch (error) {
      console.error(error)
      this.$router.push('/dashboard/owners')
    }
  },
  computed: {
    ...mapGetters({ owner: 'setOwner' })
  },
  methods: {
    ...mapActions(['updateOwner', 'viewOwner']),
    async submit () {
      try {
        const owner = {
          id: this.id,
          form: this.form
        }
        await this.updateOwner(owner)
        this.$router.push({ name: 'Owner', params: { id: this.owner.id } })
      } catch (error) {
        console.log(error)
      }
    }
  }
})
</script>
