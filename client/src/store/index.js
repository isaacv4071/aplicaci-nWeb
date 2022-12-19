import { createStore } from 'vuex'

import notes from './modules/notes'
import users from './modules/user'
import owners from './modules/owners'

export default createStore({
  modules: {
    notes,
    users,
    owners
  }
})
