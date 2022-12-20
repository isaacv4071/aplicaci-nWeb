<template>
  <section>
    <h1>Tú Perfil</h1>
    <hr />
    <br />
    <div>
      <p>
        <strong>Nombre Completo:</strong> <span>{{ user.full_name }}</span>
      </p>
      <p>
        <strong>Nombre de Usuario:</strong> <span>{{ user.username }}</span>
      </p>
      <p>
        <button @click="deleteAccount()" class="btn btn-primary">
          Eliminar Cuenta
        </button>
      </p>
    </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue'
import { mapGetters, mapActions } from 'vuex'

export default defineComponent({
  name: 'ProfileView',
  created: function () {
    return this.$store.dispatch('viewMe')
  },
  computed: {
    ...mapGetters({ user: 'stateUser' })
  },
  methods: {
    ...mapActions(['deleteUser']),
    async deleteAccount () {
      try {
        await this.deleteUser(this.user.id)
        await this.$store.dispatch('logOut')
        this.$router.push('/')
      } catch (error) {
        console.error(error)
      }
    }
  }
})
</script>
