import httpBeautify from "http-beautify";
import http from "./http";

class Categories extends httpBeautify {
	constructor(id) {
		const resource = "/api/categories";
		const relationship = {};
		super(id, relationship, resource, http);
	}
}

export default (id) => new Categories(id);
