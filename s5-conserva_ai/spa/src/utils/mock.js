export function getImagesMock(limit = 5, img = "https://picsum.photos/1920/1080?random") {
	let images = [];

	for (let i = 1; i < limit + 1; i++) {
		images.push({ id: i, url: img });
	}

	return images;
}

export function getExamplesMock() {
	let examples = [];
	let names = ["ex1", "ex2", "ex3"];
	for (let name in names) {
		examples.push({ name: names[name], active: false });
	}
	return examples;
}

export function getItemsMock() {
	return [
		{
			id: 1,
			level: "0",
			color: "var(--v-neutralgray-base)",
		},
		{
			id: 2,
			level: "1",
			color: "var(--v-green-base)",
		},
		{
			id: 3,
			level: "2",
			color: "var(--v-lightblue-base)",
		},
		{
			id: 4,
			level: "3",
			color: "var(--v-primary-base)",
		},
		{
			id: 5,
			level: "4",
			color: "var(--v-orange-base)",
		},
		{
			id: 6,
			level: "5",
			color: "var(--v-red-base)",
		},
		{
			id: 7,
			level: "?",
			color: "var(--v-magenta-base)",
		},
	];
}
