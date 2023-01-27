import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import RegisterView from '@/views/users/RegisterView.vue'
import LoginView from '@/views/users/LoginView.vue'
import DashboardView from '@/views/DashboardView.vue'
import ProfileView from '@/views/users/ProfileView.vue'
import OwnersView from '@/views/owners/OwnersView.vue'
import OwnerView from '@/views/owners/OwnerView.vue'
import EditOwnerView from '@/views/owners/EditOwnerView.vue'
import EditVehicleView from '@/views/vehicles/EditVehicleView.vue'
import VehicleView from '@/views/vehicles/VehicleView.vue'
import VehiclesView from '@/views/vehicles/VehiclesView.vue'
import store from '@/store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardView,
    meta: { requiresAuth: true },
    children: [
      {
        name: 'Owners',
        path: '/dashboard/owners',
        component: OwnersView,
        meta: { requiresAuth: true }
      },
      {
        name: 'Owner',
        path: '/dashboard/owner/:id',
        component: OwnerView,
        meta: { requiresAuth: true },
        props: true
      },
      {
        name: 'OwnerEdit',
        path: '/dashboard/edit/owner/:id',
        component: EditOwnerView,
        meta: { requiresAuth: true },
        props: true
      },
      {
        name: 'Vehicles',
        path: '/dashboard/vehicles',
        component: VehiclesView,
        meta: { requiresAuth: true }
      },
      {
        name: 'Vehicle',
        path: '/dashboard/vehicle/:id',
        component: VehicleView,
        meta: { requiresAuth: true },
        props: true
      },
      {
        name: 'VehicleEdit',
        path: '/dashboard/edit/vehicle/:id',
        component: EditVehicleView,
        meta: { requiresAuth: true },
        props: true
      }
    ]
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, _, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next()
      return
    }
    next('/')
  } else {
    next()
  }
})

export default router
