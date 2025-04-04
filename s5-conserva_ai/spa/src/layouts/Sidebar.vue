<template>
	<v-navigation-drawer color="white" fixed elevation-1 :value="collapsedHandle" width="240" app>
		<v-list-item>
			<v-list-item-content>
				<v-list-item-title>
					<v-img
						class="mt-5 ml-4"
						width="160"
						height="60"
						:src="require('@/assets/icons/conservai-logo.png')"
					/>
				</v-list-item-title>
			</v-list-item-content>
		</v-list-item>
		<div class="line"></div>
		<div class="sidebar pt-12">
			<ul class="tree pl-0">
				<div v-for="(item, index) in items" :key="index">
					<li class="mb-5">
						<router-link
							active-class="routerlink-item-active"
							:to="item.route"
							class="ml-1 text-decoration-none d-flex justify-space-between pa-1"
						>
							<div>
								<v-icon size="20" color="accent" class="ml-1 mb-1 mt-1 mr-1">{{ item.icon }}</v-icon>
								{{ item.text }}
							</div>
							<v-icon v-if="isActiveRoute(item)">mdi-chevron-right</v-icon>
						</router-link>
						<ul v-if="item.children" class="tree-cl text-left ml-n0">
							<li v-for="(subitem, subindex) in item.children" :key="subindex">
								<span class="tree_label text-left">
									<router-link
										active-class="active-sub-route"
										class="text-decoration-none"
										:to="subitem.route"
									>
										{{ subitem.text }}
									</router-link>
								</span>
							</li>
						</ul>
					</li>
				</div>
			</ul>
			<div class="line-exit"></div>
			<div class="exit-icon pa-1" @click="logout">
				<v-icon size="30" left>mdi-exit-to-app</v-icon>
				<span>Sair</span>
			</div>
		</div>
	</v-navigation-drawer>
</template>

<script>
export default {
	name: "RocketNavigation",
	props: {
		collapsed: {
			type: Boolean,
			default: () => true,
		},
	},
	data() {
		return {
			collapsedHandle: true,
			items: [
				{
					text: "Dashboard",
					icon: "mdi-clipboard-text-outline",
					route: "/dashboard",
					// roleRequired: "Teste",
				},
				{
					text: "Estoque",
					icon: "mdi-archive-search-outline",
					route: "/stock",
					// roleRequired: "Teste",
				},
				{
					text: "Gerenciamento",
					icon: "mdi-table-edit",
					route: "/management",
					// roleRequired: "Teste",
				},
				// {
				// 	text: "Relatórios",
				// 	icon: "mdi-text-box-multiple-outline",
				// 	route: "/reports",
				// 	// roleRequired: "Teste",
				// },
				// {
				// 	text: "Receitas",
				// 	icon: "mdi-book-open-outline",
				// 	route: "/recipes",
				// 	// roleRequired: "Teste",
				// },
				// {
				// 	text: "Perfil",
				// 	icon: "mdi-account-outline",
				// 	route: "/profile",
				// 	// roleRequired: "Teste",
				// },
			],
		};
	},
	watch: {
		collapsed(value) {
			this.collapsedHandle = value;
		},
	},

	methods: {
		handleRoute(route) {
			this.$router.push(route);
		},
		isActiveRoute(item) {
			return this.$route.path == item.route;
		},
		logout() {
			this.$keycloak.logout();
		},
	},
};
</script>
<style scoped>
.active,
.active-sub-route {
	color: var(--v-primary-base) !important;
	font-weight: 700;
}

.active i {
	color: var(--v-primary-base) !important;
}

.active::before {
	position: absolute;
	top: 3px;
	bottom: 0;
	left: 1em;
	height: 20px;
	display: block;
	width: 0;
	border-left: 4px solid var(--v-primary-base);
	content: "";
}

.active a:before {
	position: absolute;
	top: 0;
	bottom: 0;
	left: -0.7em;
	display: block;
	width: 0;
	border-left: 1px solid #c4c4c4;
	content: "";
}

.sidebar ul {
	list-style: none;
}

.sidebar ul li a {
	font-style: normal;
	font-weight: 400;
	font-size: 14px;
	line-height: 14px;
	color: var(--v-secondary-base);
	line-height: 16px;
}

.sidebar span {
	font-style: normal;
	font-weight: 400;
	font-size: 20px;
	line-height: 14px;
	line-height: 16px;
	padding-top: 5px;
}

.tree {
	text-align: left;
	margin: 1em;
}

.tree input ~ ul {
	display: none;
}

.tree input:checked ~ ul {
	display: block;
}

.tree li {
	line-height: 1.2;
	position: relative;
	padding: 0 0 1em 1em;
}

.tree ul li {
	padding: 1em 0 0 1em;
}

.tree > li:last-child {
	padding-bottom: 0;
}

.tree_label {
	position: relative;
	display: inline-block;
	cursor: pointer;
	font-style: normal;
	font-weight: 400;
	font-size: 14px;
	line-height: 14px;
	color: var(--v-accent-base);
	line-height: 16px;
}

label.tree_label:before {
	background: #000;
	color: #fff;
	position: relative;
	z-index: 1;
	float: left;
	margin: 0 1em 0 -2em;
	width: 1em;
	height: 1em;
	border-radius: 1em;
	text-align: center;
	line-height: 0.9em;
}

.tree-cl li:before {
	position: absolute;
	top: 0;
	bottom: 0;
	left: -0.5em;
	display: block;
	width: 0;
	border-left: 1px solid var(--v-accent-base);
	content: "";
}

.tree_label:only-child:after {
	position: absolute;
	top: 0;
	left: -1.7em;
	display: block;
	height: 0.5em;
	width: 1em;
	border-bottom: 1px solid var(--v-accent-base);
	border-left: 1px solid var(--v-accent-base);
	border-radius: 0 0 0 0.3em;
	content: "";
}

.tree li:last-child:before {
	height: 1em;
	bottom: auto;
}

.tree > li:last-child:before {
	display: none;
}

.line-exit {
	width: 100%;

	border-bottom: 1px solid #ba0000;
	position: absolute;
	bottom: 140px;
}

.line {
	width: 100%;
	height: 25px;
	border-bottom: 1px solid #ba0000;
	position: absolute;
}
.item-text {
	font-size: 16px !important;
}

.exit-icon {
	display: flex;
	position: absolute;
	bottom: 3rem;
	left: 2.5rem;
	color: #ba0000;
	cursor: pointer;
}

.exit-icon .v-icon {
	color: #ba0000;
	transform: scaleX(-1);
	margin-top: -2px;
}

.routerlink-item-active {
	/* background-color: var(--v-primary-base); */
	background-color: #3470255e;
	font-weight: 700 !important;
}
</style>
