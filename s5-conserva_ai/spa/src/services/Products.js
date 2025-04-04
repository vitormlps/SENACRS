import httpBeautify from "http-beautify";
import http from "./http";

class Products extends httpBeautify {
	constructor(id) {
		const resource = "/api/products";
		const relationship = {
			categories: "categories",
		};
		super(id, relationship, resource, http);
	}
}

export default (id) => new Products(id);
