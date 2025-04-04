import Vue from "vue";
import Swal from "sweetalert2";

const SweetAlert = {
	confirm(text = "Confirmar", title = "", confirmText = "Confirmar", cancelText = "Cancelar") {
		return Swal.fire({
			title,
			text,
			// icon: "question",
			confirmButtonText: confirmText,
			confirmButtonColor: "#5F9551",
			showCancelButton: true,
			cancelButtonText: cancelText,
			cancelButtonColor: "#D24444",
			allowOutsideClick: true,
			timer: 12000,
			timerProgressBar: true,
		}).then((result) => {
			if (result.value) {
				return Promise.resolve();
			} else {
				return Promise.reject();
			}
		});
	},
};

Vue.prototype.$swal = SweetAlert;
export default SweetAlert;
