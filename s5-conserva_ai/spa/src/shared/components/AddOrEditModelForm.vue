<template>
	<FormModal :title="titleDialog" :dialog="dialog" @closeForm="closeForm" @store="addOrUpdate">
		<v-form ref="formItem">
			<v-text-field
				v-for="field in fieldtemplate"
				:key="field"
				height="40"
				v-model="form[field]"
				outlined
				:label="translateToPortuguese(field)"
				solo
				:rules="[rules.required]"
				flat
			/>
		</v-form>
	</FormModal>
</template>

<script>
import FormModal from "@/shared/components/FormModal.vue";
import rules from "@/shared/mixins/rules";
import toastify from "@/utils/toast";
import { translateService } from "@/utils/translations";

export default {
	components: {
		FormModal,
	},
	mixins: [rules],
	props: {
		title: {
			type: String,
			default: String(),
		},
		httpService: {
			type: Object,
			default: () => {},
		},
		selectedItem: {
			type: Object,
			default: () => {},
		},
		itemTemplate: {
			type: Array,
			default: () => [],
		},
		handlerDialog: {
			type: Boolean,
			default: false,
		},
	},
	data() {
		return {
			titleDialog: "",
			dialog: false,
			form: {},
			fieldtemplate: [],
		};
	},

	methods: {
		translateToPortuguese(field) {
			field = translateService(field);
			let temp = field.slice(-2);
			if (temp == "õe") {
				temp = "ão";
			}
			return field.slice(0, -2) + temp;
		},

		cleanTemplate() {
			const temp = [];
			this.itemTemplate.forEach((field) => {
				if (!["id", "createdAt", "updatedAt"].includes(field)) {
					temp.push(field);
				}
			});
			this.fieldtemplate = temp;
		},

		closeForm() {
			this.$emit("closeForm");
			this.$refs.formItem.reset();
		},

		async add() {
			return await this.httpService.store(this.form);
		},

		async update() {
			delete this.form.created_at;
			delete this.form.updated_at;
			this.httpService["id"] = "/" + this.selectedItem.id;
			return await this.httpService.update(this.form);
		},

		async addOrUpdate() {
			if (!this.$refs.formItem.validate()) return;
			const request = Object.keys(this.selectedItem).length === 0 ? await this.add() : await this.update();
			if (toastify(request)) {
				this.closeForm();
			}
		},
	},
	watch: {
		handlerDialog(value) {
			this.cleanTemplate();
			this.dialog = value;
			this.titleDialog = "Adicionar " + this.title;
		},

		selectedItem(value) {
			this.cleanTemplate();
			if (Object.keys(value).length === 0) return;
			this.titleDialog = "Alterar " + this.title;
			this.form = value;
		},
	},
};
</script>
<style scoped>
.v-form .v-text-field {
	border-radius: 0 !important;
}
</style>
