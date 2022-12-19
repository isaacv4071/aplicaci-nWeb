<template>
  <div class="card text-center">
    <div class="card-header">Propietario</div>
    <div class="card-body">
      <dl>
        <dt>Documento de identidad</dt>
        <dd>{{ owner.id }}</dd>
        <dt>Tipo de Documento de identidad</dt>
        <dd>{{ owner.document_type }}</dd>
        <dt>Nombre Completo</dt>
        <dd>{{ owner.full_name }}</dd>
        <dt>Dirección</dt>
        <dd>{{ owner.address }}</dd>
        <dt>Numero de Telefono</dt>
        <dd>{{ owner.phone }}</dd>
        <dt>Correo Electronico</dt>
        <dd>{{ owner.email }}</dd>
      </dl>
    </div>
    <div class="card-footer text-muted text-center">
      <router-link to="/dashboard/owners" class="btn">Atras</router-link>
      <button @click="removeNote()" class="btn">Eliminar</button>
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue'
import { mapGetters, mapActions } from 'vuex'

export default defineComponent({
  name: 'OwnerView',
  props: ['id'],
  async created () {
    try {
      await this.viewOwner(this.id)
    } catch (error) {
      console.error(error)
      this.$router.push('/dashboard/owners')
    }
  },
  computed: {
    ...mapGetters({ owner: 'setOwner' })
  },
  methods: {
    ...mapActions(['viewOwner', 'deleteOwner']),
    async removeNote () {
      try {
        const text = '¿Desea borrar el propietario?'
        /* eslint-disable */
        if (confirm(text) == true) {
          await this.deleteOwner(this.id)
          this.$router.push('/dashboard/owners')
        } else {
          this.$router.push(`/dashboard/owner/${this.id}`)
        }
      } catch (error) {
        console.error(error)
      }
    }
  }
})
</script>
