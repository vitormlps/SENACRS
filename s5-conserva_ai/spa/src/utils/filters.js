import Vue from "vue";
import moment from "moment";

Vue.filter("formatDate", function (value) {
	if (value) {
		return moment(String(value)).format("DD-MM-YYYY HH:mm");
	}
});

Vue.filter("formatOnlyTime", function (value) {
	if (value) {
		return moment(String(value)).format("HH:mm:ss");
	}
});

Vue.filter("formatOnlyDate", function (value) {
	if (value) {
		return moment(value.toString()).format("DD/MM/YYYY");
	}
});

export default {
	formatDate: Vue.filter("formatDate"),
	formatOnlyDate: Vue.filter("formatOnlyDate"),
	formatOnlyTime: Vue.filter("formatOnlyTime"),
};
