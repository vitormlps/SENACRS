// Local imports
const Product = require("../database/models/product");
const CategoryProducts = require("../database/models/categoryProducts");
// const transactionsController = require("../controllers/transactions");

exports.findAll = async (req, res) => {
  let products = [];

  try {
    products = await Product.findAll();
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (products.length == 0) {
    return res.status(404).json({ Erro: "Não há produtos cadastrados." });
  } else {
    return res.send(products);
  }
};

exports.findById = async (req, res) => {
  const paramsId = req.params.id;
  let product = null;

  try {
    product = await Product.findByPk(paramsId);
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!product) {
    return res.status(404).json({ Erro: "Produto não encontrado." });
  } else {
    return res.send(product);
  }
};

exports.create = async (req, res) => {
  const payload = req.body;
  let product = null;

  if (!payload) {
    return res.status(400).json({
      Erro: "Requisição inválida.",
    });
  }

  try {
    product = await Product.create(payload);
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!product) {
    return res
      .status(400)
      .json({ Erro: "Não foi possível cadastrar o produto." });
  } else {
    return res.send(product);
  }
};

exports.updateById = async (req, res) => {
  const paramsId = req.params.id;
  const payload = req.body;
  let product = null;

  try {
    product = await Product.update(payload, {
      where: {
        id: paramsId,
      },
      returning: true,
    });

    product = product[1][0];
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!product) {
    return res.status(404).json({ Erro: "Produto não encontrado." });
  } else {
    return res.send(product);
  }
};

exports.deleteById = async (req, res) => {
  const paramsId = req.params.id;
  let product = null;

  try {
    product = await Product.destroy({
      where: {
        id: paramsId,
      },
    });
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!product) {
    return res.status(404).json({ Erro: "Produto não encontrado." });
  } else {
    return res.json({ Message: "Produto removido." });
  }
};

exports.categorize = async (req, res) => {
  const payload = req.body;
  let categoryProduct = null;

  if (!payload || (!payload.productId && !payload.categoryId)) {
    return res.status(400).json({
      Erro: "Requisição inválida.",
    });
  }

  try {
    categoryProduct = await CategoryProducts.create(payload);
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!categoryProduct) {
    return res
      .status(400)
      .json({ Erro: "Não foi possível categorizar o produto." });
  } else {
    return res.send(categoryProduct);
  }
};

exports.decategorize = async (req, res) => {
  const payload = req.body;
  let categoryProduct = null;

  if (!payload || (!payload.productId && !payload.categoryId)) {
    return res.status(400).json({
      Erro: "Requisição inválida.",
    });
  }

  try {
    categoryProduct = await CategoryProducts.destroy({
      where: {
        productId: payload.productId,
        categoryId: payload.categoryId,
      },
    });
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!categoryProduct) {
    return res
      .status(400)
      .json({ Erro: "Não foi possível descategorizar o produto." });
  } else {
    return res.json({ Message: "Categoria removida do produto." });
  }
};
