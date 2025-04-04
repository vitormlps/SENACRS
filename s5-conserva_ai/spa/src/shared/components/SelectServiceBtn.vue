<template>
	<v-btn
		v-if="parentCategory"
		:to="'/' + parentCategory + '/' + service"
		class="select-service-btn justify-space-between"
		elevation="0"
		tile
	>
		{{ translate }}
		<v-icon class="mr-1" size="20" color="black">mdi-chevron-right</v-icon>
	</v-btn>

	<v-btn v-else :to="'/' + service" class="select-service-btn justify-space-between" elevation="0">
		{{ translate }}
		<v-icon class="mr-1" size="20" color="black">mdi-chevron-right</v-icon>
	</v-btn>
</template>

<script>
import { translateService } from "@/utils/translations";

export default {
	name: "SelectServiceBtn",
	props: {
		parentCategory: {
			type: String,
			default: null,
		},
		service: {
			type: String,
			default: String(),
		},
	},
	data() {
		return {
			translate: "",
		};
	},
	mounted() {
		this.translate = translateService(this.service);
	},
};
</script>

<style>
.select-service-btn {
	width: 45%;
	margin: 1% 0;
	padding: 2% !important;
	color: black !important;
	background-color: white !important;
	font-weight: 900 !important;
	font-size: 18px !important;
	text-transform: capitalize !important;
	border: 1px solid rgb(223, 223, 223);
}
</style>
