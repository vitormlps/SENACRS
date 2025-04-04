class Category {
	id = 0;
	expirationDate = Date.now();
	quantity = 0;
	location = "";
	productId = 0;
}

export default () => new Category();
