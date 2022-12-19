<template>
  <header>
    <nav class="navbar navbar-expand-md">
      <div class="container">
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarCollapse"
          aria-controls="navbarCollapse"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="line" id="line"></span>
          <span class="line"></span>
          <span class="line"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul v-if="isLoggedIn" class="navbar-nav me-auto mb-2 mb-md-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/dashboard"
                >Dashboard</router-link
              >
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/profile"
                >My Profile</router-link
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" @click="logout">Log Out</a>
            </li>
          </ul>
          <ul v-else class="navbar-nav me-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/register"
                >Register</router-link
              >
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/login">Log In</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'NavBar',
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated
    }
  },
  methods: {
    async logout () {
      await this.$store.dispatch('logOut')
      this.$router.push('/login')
    }
  }
})
</script>

<style scoped>
a {
  cursor: pointer;
}

.navbar {
  background-color: #4b6584;
}

.nav-link {
  color: white;
  font-weight: bold;
}

.navbar-toggler {
  width: 47px;
  height: 34px;
  background-color: #a5b1c2;
  border: none;
  padding: 9px 12px;
}
.navbar-toggler .line {
  width: 100%;
  float: left;
  height: 2px;
  background-color: #4b6584;
  margin-bottom: 5px;
}

</style>
