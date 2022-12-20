<template>
  <h2 class="text-center">Dashboard</h2>
  <div class="d-grid gap-2 d-md-block text-center">
    <router-link class="btn btn-primary" to="/dashboard/owners"
      >Propietarios</router-link
    >
    <router-link class="btn btn-primary" to="/dashboard/vehicles"
      >Vehículos</router-link
    >
  </div>
  <div class="container"><router-view /></div>
</template>
<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'DashboardView'
})
</script>
