import Vue from "vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import "@mdi/font/css/materialdesignicons.css";

Vue.use(Vuetify);

const opts = {
	icons: {
		defaultSet: "mdi",
	},
	theme: {
		options: {
			customProperties: true,
		},
		themes: {
			light: {
				// primary: "#00c088",
				primary: "#5F9551",
				background: "#F5F5F5",
				secondary: "#424242",
				accent: "#5F5F5F",
				black: "#151515",
				gray: "#c4c4c4",
				error: "#FF5252",
				info: "#d9d9d9",
				success: "#4CAF50",
				warning: "#FFC107",
				lightblue: "#14c6FF",
				yellow: "#FFCF00",
				pink: "#FF1976",
				orange: "#FF8657",
				magenta: "#C33AFC",
				darkblue: "#1E2D56",
				neutralgray: "#9BA6C1",
				green: "#2ED47A",
				red: "#FF5c4E",
				darkblueshade: "#308DC2",
				lightgray: "#BDBDBD",
				lightpink: "#FFCFE3",
				white: "#FFFFFF",
			},
		},
	},
};

export default new Vuetify(opts);
