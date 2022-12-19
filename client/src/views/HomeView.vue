<template>
  <div class="card">
    <div class="card-header">Inventario VYP</div>
    <div class="card-body">
      <p class="card-text">
        Web sencilla que permita llevar el inventario de un grupo de vehículos y
        sus propietarios.
      </p>
      <h5 v-if="isLoggedIn" class="card-title">Bienvenido@</h5>
      <div v-else>
        <div class="d-grid gap-2 d-md-block">
          <a href="/register" class="btn">Register</a>
          <span class="text-center"> or </span>
          <a href="/login" class="btn">Log In</a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HomeView',
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated
    }
  }
})
</script>

<style scoped>
.card-header{
  background-color: #4b6584;
  color: white;
  font-weight: bold;
}

.btn{
  background-color: #a5b1c2;
  color: #4b6584;
  font-weight: bold;
}
</style>
