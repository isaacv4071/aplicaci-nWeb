import axios from 'axios'

const state = {
  vehicles: null,
  vehicle: null
}

const getters = {
  setVehicles: (state) => state.vehicles,
  setVehicle: (state) => state.vehicle
}

const actions = {
  async createVehicle ({ dispatch }, vehicle) {
    await axios.post('vehicles', vehicle)
    await dispatch('getVehicles')
  },
  async getVehicles ({ commit }) {
    const { data } = await axios.get('vehicles')
    commit('setVehicles', data)
  },
  async viewVehicle ({ commit }, id) {
    const { data } = await axios.get(`vehicle/${id}`)
    commit('setVehicle', data)
  },
  // eslint-disable-next-line no-empty-pattern
  async updateVehicle ({}, vehicle) {
    await axios.patch(`vehicle/${vehicle.id}`, vehicle.form)
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteVehicle ({}, id) {
    await axios.delete(`vehicle/${id}`)
  }
}

const mutations = {
  setVehicles (state, vehicles) {
    state.vehicles = vehicles
  },
  setVehicle (state, vehicle) {
    state.vehicle = vehicle
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
