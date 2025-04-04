<template>
	<v-dialog :value="dialog" transition="dialog-bottom-transition" width="20%" persistent>
		<v-card outlined tile>
			<div class="px-6 pt-3">
				<span class="font-weight-bold" style="font-size: 1.25rem">{{ title }}</span>
				<div class="pt-6">
					<slot></slot>
				</div>
				<v-card-actions class="d-flex justify-end">
					<v-btn class="btn-text cancel" width="30%" elevation="0" @click="close" tile small depressed
						>Cancelar</v-btn
					>
					<v-btn class="btn-text accept" width="30%" elevation="0" @click="store" tile small depressed
						>Salvar</v-btn
					>
				</v-card-actions>
			</div>
		</v-card>
	</v-dialog>
</template>
<script>
export default {
	name: "FormModal",
	props: {
		title: {
			type: String,
			default: "",
		},
		dialog: {
			type: Boolean,
			default: false,
		},
	},
	methods: {
		close() {
			this.$emit("closeForm");
		},
		store() {
			this.$emit("store");
		},
	},
};
</script>
<style scoped>
.v-card__actions {
	padding: 2% 0;
}

.accept {
	background-color: #5f9551 !important;
}

.cancel {
	background-color: #d24444 !important;
}
</style>
