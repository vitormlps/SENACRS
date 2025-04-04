import httpBeautify from "http-beautify";
import http from "./http";

class Batches extends httpBeautify {
	constructor(id) {
		const resource = "/api/batches";
		const relationship = {
			categories: "categories",
		};
		super(id, relationship, resource, http);
	}
}

export default (id) => new Batches(id);
