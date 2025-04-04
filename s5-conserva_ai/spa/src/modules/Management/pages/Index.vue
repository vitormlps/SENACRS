<template>
	<div class="container">
		<router-view />
		<h1 class="mb-5">{{ categoryTitle }}</h1>

		<div class="d-flex" v-for="item in items" :key="item">
			<SelectServiceBtn :parentCategory="categoryUri" :service="item" />
		</div>
	</div>
</template>

<script>
import SelectServiceBtn from "@/shared/components/SelectServiceBtn.vue";

export default {
	components: {
		SelectServiceBtn,
	},
	data: () => ({
		categoryTitle: "Gerenciamento",
		categoryUri: "management",
		items: ["products", "batches", "categories"],
	}),
	mounted() {},
	computed: {},
	methods: {},
};
</script>

<style scoped>
.container {
	margin-left: 0.7%;
}
</style>
