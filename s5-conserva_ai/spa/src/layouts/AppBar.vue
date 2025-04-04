<template>
	<v-app-bar color="background" app elevation="0">
		<!-- <v-app-bar-nav-icon class="mr-3" @click="handleSidebar"></v-app-bar-nav-icon> -->
		<v-icon class="back-btn ml-1" v-if="showBackBtn" @click="backToPreviousPage">mdi-keyboard-backspace</v-icon>
		<!-- {{ title }} -->
		<v-spacer></v-spacer>

		<div class="d-flex justify-space-between action-buttons mr-n4">
			<v-btn icon>
				<v-icon>mdi-bell-badge-outline</v-icon>
			</v-btn>

			<v-btn icon>
				<v-icon>mdi-account-circle-outline</v-icon>
			</v-btn>
		</div>
	</v-app-bar>
</template>

<script>
export default {
	name: "AppBar",
	components: {},
	data() {
		return {
			sidebarExpanded: true,
			title: "PixGrid",
			showBackBtn: false,
		};
	},
	methods: {
		handleSidebar() {
			this.sidebarExpanded = !this.sidebarExpanded;
			this.$emit("collapseSidebar", this.sidebarExpanded);
		},
		backToPreviousPage() {
			this.$router.go(-1);
		},
	},
	mounted() {
		this.title = this.$route.name;
	},
	watch: {
		$route(to, from) {
			this.title = to.name;
			this.showBackBtn = true;
		},
	},
};
</script>

<style scoped>
.action-buttons {
	width: 7rem;
}

.back-btn {
	cursor: pointer;
}

.back-btn:hover {
	color: var(--v-darkblueshade-base);
}
</style>
