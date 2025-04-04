import Index from "../components/Index.vue";
import List from "../pages/Index.vue";
import ServiceBase from "../pages/ServiceBase.vue";

export default [
	{
		path: "/management",
		component: Index,
		// meta: { isAuthenticated: true },
		redirect: "/management/list",
		children: [
			{
				path: "list",
				name: "Gerenciamento",
				component: List,
				// meta: { isAuthenticated: true },
			},
			{
				path: "products",
				name: "Produtos",
				component: ServiceBase,
				// meta: { isAuthenticated: true },
			},
			{
				path: "batches",
				name: "Lotes",
				component: ServiceBase,
				// meta: { isAuthenticated: true },
			},
			{
				path: "categories",
				name: "Categorias",
				component: ServiceBase,
				// meta: { isAuthenticated: true },
			},
		],
	},
];
