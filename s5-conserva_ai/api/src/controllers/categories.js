// Local imports
const Category = require("../database/models/category");

exports.findAll = async (req, res) => {
  let categories = [];

  try {
    categories = await Category.findAll();
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (categories.length == 0) {
    return res.status(404).json({ Erro: "Não há categorias cadastradas." });
  } else {
    return res.send(categories);
  }
};

exports.findById = async (req, res) => {
  const paramsId = req.params.id;
  let category = null;

  try {
    category = await Category.findByPk(paramsId);
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!category) {
    return res.status(404).json({ Erro: "Categoria não encontrada." });
  } else {
    return res.send(category);
  }
};

exports.create = async (req, res) => {
  const payload = req.body;
  let category = null;

  if (!payload) {
    return res.status(400).json({
      Erro: "Requisição inválida.",
    });
  }

  try {
    category = await Category.create(payload);
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!category) {
    return res
      .status(400)
      .json({ Erro: "Não foi possível cadastrar a categoria." });
  } else {
    return res.send(category);
  }
};

exports.updateById = async (req, res) => {
  const paramsId = req.params.id;
  const payload = req.body;
  let category = null;

  try {
    category = await Category.update(payload, {
      where: {
        id: paramsId,
      },
      returning: true,
    });

    category = category[1][0];
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!category) {
    return res.status(404).json({ Erro: "Categoria não encontrada." });
  } else {
    return res.send(category);
  }
};

exports.deleteById = async (req, res) => {
  const paramsId = req.params.id;
  let category = null;

  try {
    category = await Category.destroy({
      where: {
        id: paramsId,
      },
    });
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!category) {
    return res.status(404).json({ Erro: "Categoria não encontrada." });
  } else {
    return res.json({ Message: "Categoria removida." });
  }
};
