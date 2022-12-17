import { createStore } from 'vuex'

import notes from './modules/notes'
import users from './modules/user'

export default createStore({
  modules: {
    notes,
    users
  }
})
