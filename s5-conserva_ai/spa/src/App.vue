<template>
	<v-app id="app" class="background">
		<AppBar @collapseSidebar="handleSidebar($event)" />
		<Sidebar :collapsed="handleCollapse" />
		<v-main>
			<router-view />
		</v-main>
	</v-app>
</template>

<script>
import { defineComponent } from "@vue/composition-api";
import AppBar from "./layouts/AppBar.vue";
import Sidebar from "./layouts/Sidebar.vue";

export default defineComponent({
	name: "App",
	components: {
		AppBar,
		Sidebar,
	},
	data() {
		return {
			handleCollapse: true,
		};
	},
	methods: {
		handleSidebar(boolean) {
			this.handleCollapse = boolean;
		},
	},
});
</script>

<style>
.v-application {
	background: var(--v-background-base) !important;
}
</style>
