import axios from "axios";
import Vue from "vue";

const http = axios.create({
	baseURL: import.meta.env.VITE_API,
	timeout: 120000,
	headers: { "Content-Type": "multipart/form-data" },
});

// http.interceptors.request.use(
// 	(config) => {
// 		const token = Vue.$keycloak.token;
// 		if (token) config.headers.Authorization = `Bearer ${token}`;
// 		return config;
// 	},
// 	(error) => Promise.reject(error)
// );

http.interceptors.response.use(
	(response) => {
		return response;
	},
	(error) => {
		if (error.response !== undefined) {
			if (error.response.status === 401) {
				// Vue.$keycloak.logout()
			}
		}
		return Promise.reject(error);
	}
);

export default http;
