export function translateService(service) {
	let temp = "";

	switch (service) {
		case "user":
			temp = "Usuário";
			break;
		case "products":
			temp = "Produtos";
			break;
		case "batches":
			temp = "Lotes";
			break;
		case "categories":
			temp = "Categorias";
			break;
		case "transactions":
			temp = "Transações";
			break;
		case "stock":
			temp = "Estoque";
			break;
		case "name":
			temp = "Nome";
			break;
		case "id":
			temp = "ID";
			break;
		case "productId":
			temp = "ID do Produto";
			break;
		case "description":
			temp = "Descrição";
			break;
		case "minQty":
			temp = "Qtd. Min";
			break;
		case "maxQty":
			temp = "Qtd. Max";
			break;
		case "measurementUnit":
			temp = "Medida";
			break;
		case "expirationDate":
			temp = "Validade";
			break;
		case "quantity":
			temp = "Quantidade";
			break;
		case "location":
			temp = "Local";
			break;
		case "email":
			temp = "E-mail";
			break;
		case "password":
			temp = "Senha";
			break;
		case "createdAt":
			temp = "Criado em";
			break;
		case "updatedAt":
			temp = "Atualizado em";
			break;
		case "lastUpdate":
			temp = "Última atualização";
			break;
		case "mostRecentExpireDate":
			temp = "A expirar";
			break;
		case "batchesSum":
			temp = "Qtd. Lotes";
			break;
		case "qtySum":
			temp = "Qtd. Total";
			break;

		default:
			temp = "Serviço";
			break;
	}

	return temp;
}
