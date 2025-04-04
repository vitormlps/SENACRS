import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import sweetalert2 from "@/shared/plugins/sweet-alert";
import filters from "./utils/filters";
import VueCompositionApi from "@vue/composition-api";
import vuetify from "./vuetify";
import "./styles/main.css";
import store from "./store";

Object.keys(filters).forEach((key) => {
	Vue.filter(key, filters[key]);
});

Vue.use(VueCompositionApi);

new Vue({
	router,
	store,
	vuetify,
	sweetalert2,
	render: (h) => h(App),
}).$mount("#app");
