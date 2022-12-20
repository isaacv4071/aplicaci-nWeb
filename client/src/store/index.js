import { createStore } from 'vuex'

import users from './modules/user'
import owners from './modules/owners'
import vehicles from './modules/vehicles'

export default createStore({
  modules: {
    users,
    owners,
    vehicles
  }
})
