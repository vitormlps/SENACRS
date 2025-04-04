import httpBeautify from "http-beautify";
import http from "./http";

class Users extends httpBeautify {
	constructor(id) {
		const resource = "/api/users";
		const relationship = {};
		super(id, relationship, resource, http);
	}
}

export default (id) => new Users(id);
