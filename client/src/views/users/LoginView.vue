<template>
  <div
    id="card"
    class="card text-center position-absolute top-50 start-50 translate-middle"
  >
    <div class="card-body">
      <h5>VYP</h5>
      <i class="bi bi-person-circle" id="logo"></i>
      <form @submit.prevent="submit">
        <div v-if="error" class="alert alert-danger">{{ error }}</div>
        <div class="mb-3">
          <input
            type="text"
            name="username"
            v-model="form.username"
            class="form-control"
            placeholder="Usuario"
            required
          />
        </div>
        <div class="mb-3">
          <input
            type="password"
            name="password"
            v-model="form.password"
            class="form-control"
            placeholder="Contraseña"
            required
          />
        </div>
        <button type="submit" class="btn">Iniciar sesión</button>
      </form>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { mapActions } from 'vuex'

export default defineComponent({
  name: 'LoginView',
  data () {
    return {
      form: {
        username: '',
        password: ''
      },
      error: null
    }
  },
  methods: {
    ...mapActions(['logIn']),
    async submit () {
      const User = new FormData()
      User.append('username', this.form.username)
      User.append('password', this.form.password)
      try {
        await this.logIn(User)
        this.$router.push('/dashboard')
      } catch (error) {
        this.error = 'usuario o contraseña invalido'
      }
    }
  }
})
</script>
<style scoped>
#logo {
  font-size: 80px;
}
</style>
