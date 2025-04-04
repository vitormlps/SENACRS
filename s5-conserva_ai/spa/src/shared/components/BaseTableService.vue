<template>
	<div>
		<div class="d-flex justify-end ml-7 mr-14">
			<div class="search-bar">
				<v-text-field
					height="36"
					v-model="search"
					:label="`Pesquisar ${$route.name.toLowerCase()}`"
					prepend-inner-icon="mdi-magnify"
					outlined
					solo
					clearable
					flat
				/>
			</div>
			<v-btn
				v-if="parentCategory != 'Estoque'"
				class="ml-15"
				color="btn-text primary"
				elevation="0"
				@click="addOrUpdateItem()"
				tile
			>
				<v-icon size="22"> mdi-plus </v-icon>
				Adicionar {{ translate }}
			</v-btn>
		</div>

		<div>
			<v-data-table
				class="table-container ml-4 mr-10 mb-4"
				sort-by="id"
				:headers="headers"
				:items="items"
				:search="search"
				:items-per-page="5"
				:footer-props="{ itemsPerPageText: 'Linhas por página' }"
			>
				attrs[0] == "lastUpdate" || attrs[0] == "mostRecentExpireDate"

				<template v-slot:[`item.createdAt`]="{ item }">
					{{ item.createdAt | formatOnlyDate }}
				</template>
				<template v-slot:[`item.lastUpdate`]="{ item }">
					{{ item.lastUpdate | formatOnlyDate }}
				</template>
				<template v-slot:[`item.expirationDate`]="{ item }">
					<span v-if="isDate(item.expirationDate)" class="expired">
						<strong>{{ item.expirationDate | formatOnlyDate }}</strong>
					</span>
					<span v-else class="not-expired">
						<strong>{{ item.expirationDate | formatOnlyDate }}</strong>
					</span>
				</template>
				<template v-slot:[`item.mostRecentExpireDate`]="{ item }">
					<span v-if="isDate(item.mostRecentExpireDate)" class="expired">
						<strong>{{ item.mostRecentExpireDate | formatOnlyDate }}</strong>
					</span>
					<span v-else class="not-expired">
						<strong>{{ item.mostRecentExpireDate | formatOnlyDate }}</strong>
					</span>
				</template>
				<template v-slot:[`item.updatedAt`]="{ item }">
					{{ item.updatedAt | formatOnlyDate }}
				</template>
				<template v-slot:[`item.qtySum`]="{ item }">
					<span v-if="isBetweenQtys(item)" class="not-expired">
						<strong>{{ item.qtySum }}</strong>
					</span>
					<span v-else class="expired">
						<strong>{{ item.qtySum }}</strong>
					</span>
				</template>

				<template v-slot:[`item.actions`]="{ item }">
					<v-btn
						v-if="service != 'Categories'"
						min-width="30"
						small
						depressed
						color="info"
						text
						@click="categorizeItem(item)"
					>
						<v-icon center color="accent" size="18"> mdi-tag-plus-outline </v-icon>
					</v-btn>
					<v-btn min-width="30" small depressed color="info" text @click="addOrUpdateItem(item)">
						<v-icon center color="accent" size="18"> mdi-pencil-outline </v-icon>
					</v-btn>
					<v-btn min-width="30" small depressed color="info" text @click="deleteItem(item)">
						<v-icon center color="accent" size="18"> mdi-trash-can-outline </v-icon>
					</v-btn>
				</template>
			</v-data-table>
		</div>

		<AddOrEditModelForm
			:title="translate"
			:httpService="httpService"
			:selectedItem="selectedItem"
			:itemTemplate="itemTemplate"
			:handlerDialog="dialog"
			@closeForm="closeModal()"
		/>

		<!-- <CategorizeModelForm
			v-if="service != 'Categories'"
			:title="translate"
			:httpService="httpService"
			:selectedItem="selectedItem"
			:itemTemplate="itemTemplate"
			:handlerDialog="categoryDialog"
			@closeForm="closeModal()"
		/> -->
	</div>
</template>

<script>
import Header from "./Header.vue";
import AddOrEditModelForm from "./AddOrEditModelForm.vue";
// import CategorizeModelForm from "./CategorizeModelForm.vue";
import toastify from "@/utils/toast.js";
import { translateService } from "@/utils/translations.js";
import Product from "../models/Product.js";
import Batch from "../models/Batch.js";
import Category from "../models/Category.js";
import Products from "@/services/Products.js";
import Batches from "@/services/Batches.js";
// import Categories from "@/services/Categories";

export default {
	name: "BaseTableService",
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
	components: {
		Header,
		AddOrEditModelForm,
		// CategorizeModelForm,
	},
	data() {
		return {
			httpService: {},
			headers: [],
			items: [],
			search: "",
			dialog: false,
			categoryDialog: false,
			selectedItem: {},
			translate: "",
			itemTemplate: [],
		};
	},
	async mounted() {
		this.translateToPortuguese();
		if (this.parentCategory != "Estoque") {
			await this.fetchLocalServices();
			await this.fetchResource();
			this.setHeaders();
		} else {
			await this.fetchStock();
			this.setStockHeaders();
		}
		console.log(this.items);
	},
	methods: {
		translateToPortuguese() {
			this.translate = translateService(this.service.toLowerCase()).slice(0, -1);
			let temp = this.translate.slice(-2);
			if (temp == "õe") {
				temp = "ão";
			}
			this.translate = this.translate.slice(0, -2) + temp;
		},

		isDate(item) {
			let date = new Date(item);
			if (date <= Date.now()) {
				return true;
			} else {
				return false;
			}
		},

		isBetweenQtys(item) {
			if (item.minQty < item.qtySum && item.qtySum < item.maxQty) {
				return true;
			} else {
				return false;
			}
		},

		async fetchLocalServices() {
			const service = await import(`../../services/${this.service}.js`);
			this.httpService = service.default();
		},

		async fetchResource() {
			this.httpService["id"] = "";
			const { data } = await this.httpService.show();
			const tempItems = [];

			if (data) {
				data.forEach((item) => {
					let temp = Object.entries(item);

					temp = temp.filter((element) => {
						return element[0] != "password";
					});

					temp.forEach((attrs) => {
						if (attrs[0] == "createdAt" || attrs[0] == "updatedAt" || attrs[0] == "expirationDate") {
							attrs[1] = new Date(attrs[1]);
						} else {
							if (typeof attrs[1] == "object") {
								if (!attrs[1] || attrs[1].length == 0) {
									attrs[1] = 0;
								} else if (attrs[1].length > 0) {
									attrs[1] = attrs[1].length;
								} else if (attrs[1].name) {
									attrs[1] = attrs[1].name;
								} else {
									attrs[1] = attrs[1].id;
								}
							}
						}
					});
					tempItems.push(Object.fromEntries(temp));
				});
				this.items = tempItems;
			}
		},

		setHeaders() {
			let temp = null;

			if (!this.items[0]) {
				switch (this.service) {
					case "Products":
						temp = Object.keys(Product());
						break;
					case "Batches":
						temp = Object.keys(Batch());
						break;
					case "Categories":
						temp = Object.keys(Category());
						break;
					default:
						temp = Object.keys(Product());
						break;
				}
			} else {
				temp = Object.keys(this.items[0]);
			}
			this.itemTemplate = temp;

			for (let index = 0; index < temp.length; index++) {
				let head = translateService(temp[index]);

				this.headers.push({
					text: head,
					value: temp[index],
					align: "start",
					sortable: true,
				});
			}
			this.headers.push({
				text: "",
				value: "actions",
				sortable: false,
				width: "210",
			});
		},

		async fetchStock() {
			const { data } = await Products().show();
			const tempItems = [];

			if (data) {
				data.forEach(async (product) => {
					delete product.description;
					delete product.createdAt;
					product.lastUpdate = product.updatedAt;
					delete product.updatedAt;

					const batches = await Batches().show({ productId: product.id });

					product.batchesSum = batches.data ? batches.data.length : 0;
					product.qtySum = 0;

					let today = new Date();
					let tempDate = new Date();
					tempDate.setDate(tempDate.getDate() + 365);
					product.mostRecentExpireDate = today;

					let temp = null;
					if (batches.data) {
						batches.data.forEach((batch) => {
							product.qtySum += batch.quantity;

							let expireDate = new Date(batch.expirationDate);

							if (batch.expirationDate == batches.data[0].expirationDate) {
								tempDate = expireDate;
							}

							if (expireDate <= tempDate) {
								product.mostRecentExpireDate = expireDate;
							}
						});

						temp = Object.entries(product);

						temp = temp.filter((element) => {
							return element[0] != "password";
						});
						temp.forEach((attrs) => {
							if (
								attrs[0] == "createdAt" ||
								attrs[0] == "updatedAt" ||
								attrs[0] == "lastUpdate" ||
								attrs[0] == "mostRecentExpireDate"
							) {
								attrs[1] = new Date(attrs[1]);
							}
						});
						tempItems.push(Object.fromEntries(temp));
					}
				});
				this.items = tempItems;
			}
		},

		setStockHeaders() {
			let temp = ["id", "name", "batchesSum", "qtySum", "mostRecentExpireDate", "measurementUnit", "lastUpdate"];
			this.itemTemplate = temp;

			for (let index = 0; index < temp.length; index++) {
				let head = translateService(temp[index]);

				this.headers.push({
					text: head,
					value: temp[index],
					align: "start",
					sortable: true,
				});
			}
			this.headers.push({
				text: "",
				value: "actions",
				sortable: false,
				width: "210",
			});
		},

		async handleModal() {
			this.dialog = true;
		},

		async handleCategoryModal() {
			this.categoryDialog = true;
		},

		async closeModal() {
			Object.assign({}, this.selectedItem);
			this.dialog = false;
			this.categoryDialog = false;
			await this.fetchResource();
		},

		async categorizeItem(item) {
			this.selectedItem = Object.assign({}, item);
			this.handleCategoryModal();
		},

		async addOrUpdateItem(item) {
			this.selectedItem = Object.assign({}, item);
			this.handleModal();
		},

		async deleteItem(item) {
			await this.$swal.confirm(
				"Isso não pode ser desfeito!",
				`Deseja apagar o item</br>${item.name ? item.name : item.id}?`
			);
			this.httpService["id"] = "/" + item.id;
			const request = await this.httpService.delete(item.id);
			toastify(request);
			await this.fetchResource();
		},
	},
	watch: {
		service() {
			this.fetchLocalServices();
			this.fetchResource();
			this.setHeaders();
		},
	},
};
</script>

<style scoped>
.search-bar {
	width: 33% !important;
	height: 45px !important;
}

.search-bar .v-text-field {
	border-radius: 0 !important;
}

.table-container {
	padding: 0;
}

.expired {
	color: #ff5252;
}
.not-expired {
	color: #5f9551;
}
</style>
