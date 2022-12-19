<template>
  <div
    id="card"
    class="card text-center position-absolute top-50 start-50 translate-middle"
  >
    <div class="card-body">
      <h3>Register</h3>
      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input
            type="text"
            name="username"
            v-model="user.username"
            class="form-control"
            required
          />
        </div>
        <div class="mb-3">
          <label for="full_name" class="form-label">Full Name</label>
          <input
            type="text"
            name="full_name"
            v-model="user.full_name"
            class="form-control"
            required
          />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input
            type="password"
            name="password"
            v-model="user.password"
            class="form-control"
            required
          />
        </div>
        <button type="submit" class="btn">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { mapActions } from 'vuex'

export default defineComponent({
  name: 'RegisterView',
  data () {
    return {
      user: {
        username: '',
        full_name: '',
        password: ''
      }
    }
  },
  methods: {
    ...mapActions(['register']),
    async submit () {
      try {
        await this.register(this.user)
        this.$router.push('/dashboard')
      } catch (error) {
        throw new Error('Username already exists. Please try again.')
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
