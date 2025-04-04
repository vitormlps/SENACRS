import Vue from "vue";
import VueRouter from "vue-router";
import routes from "./routes";

Vue.use(VueRouter);

const router = new VueRouter({
	mode: "history",
	base: import.meta.env?.VITE_APP_PUBLIC_PATH || "/",
	routes,
});

// router.beforeEach((to, from, next) => {
//   if (to.meta.isAuthenticated) {
//     const basePath = window.location.toString();
//     if (!Vue.$keycloak.authenticated) {
//       Vue.$keycloak.login({ redirectUri: basePath });
//     }
//   }
//   next();
// });

export default router;
