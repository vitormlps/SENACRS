import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
	state: {
		entity: null,
		entities: [],
	},
	mutations: {
		setEntity(state, payload) {
			state.entity = payload;
		},
		setEntities(state, payload) {
			state.entities = payload;
		},
		addEntityToList(state, payload) {
			state.entities.push(payload);
		},
	},
});

export default store;
