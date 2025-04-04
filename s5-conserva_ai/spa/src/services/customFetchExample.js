export default async (payload) => {
	const baseURL = import.meta.env.VITE_API;
	const response = await fetch(`${baseURL}/api/endpoint-path`, {
		method: "POST",
		body: JSON.stringify(payload),
		headers: {
			"Content-Type": "application/json",
		},
	});

	if (!response.ok) {
		throw new Error(`HTTP error! status: ${response.status}`);
	}

	const textResponse = await response.text();
	return textResponse;
	// return await response.json();
};
