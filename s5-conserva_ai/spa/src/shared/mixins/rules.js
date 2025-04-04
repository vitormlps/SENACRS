const rules = {
	data() {
		return {
			rules: {
				required: (v) => !!v || "Campo não pode ser vazio",
				email: (v) => /.+@.+\..+/.test(v) || "E-mail deve ser válido",
				numeric: (v) => (v && !isNaN(v)) || "Campo deve ser numérico",
			},
		};
	},
};

export default rules;
