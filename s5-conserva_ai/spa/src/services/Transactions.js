import httpBeautify from "http-beautify";
import http from "./http";

class Transactions extends httpBeautify {
	constructor(id) {
		const resource = "/api/transactions";
		const relationship = {};
		super(id, relationship, resource, http);
	}
}

export default (id) => new Transactions(id);
