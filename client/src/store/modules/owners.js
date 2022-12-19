import axios from 'axios'

const state = {
  owners: null,
  owner: null
}

const getters = {
  setOwners: (state) => state.owners,
  setOwner: (state) => state.owner
}

const actions = {
  async createOwner ({ dispatch }, owner) {
    await axios.post('owners', owner)
    await dispatch('getOwners')
  },
  async getOwners ({ commit }) {
    const { data } = await axios.get('owners')
    commit('setOwners', data)
  },
  async viewOwner ({ commit }, id) {
    const { data } = await axios.get(`owner/${id}`)
    commit('setOwner', data)
  },
  // eslint-disable-next-line no-empty-pattern
  async updateOwner ({}, owner) {
    await axios.patch(`owner/${owner.id}`, owner.form)
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteOwner ({}, id) {
    await axios.delete(`owner/${id}`)
  }
}

const mutations = {
  setOwners (state, owners) {
    state.owners = owners
  },
  setOwner (state, owner) {
    state.owner = owner
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
