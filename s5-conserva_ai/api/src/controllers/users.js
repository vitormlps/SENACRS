// Third-party imports
const jwt = require("jsonwebtoken");
const bcrypt = require("bcrypt");

// Local imports
const User = require("../database/models/user");

exports.findAll = async (req, res) => {
  let users = [];

  try {
    users = await User.findAll();
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (users.length == 0) {
    return res.status(404).json({ Erro: "Não há usuários cadastrados." });
  } else {
    return res.send(users);
  }
};

exports.findById = async (req, res) => {
  const paramsId = req.params.id;
  let user = null;

  try {
    user = await User.findByPk(paramsId);
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!user) {
    return res.status(404).json({ Erro: "Usuário não encontrado." });
  } else {
    user = Object.assign({}, user.dataValues);
    delete user.password;
    return res.send(user);
  }
};

exports.findByEmail = async (req, res) => {
  if (!req.query && !req.query.email) {
    return res.status(400).json({
      Erro: "Requisição inválida.",
    });
  }
  let user = null;

  try {
    user = await User.findAll({
      where: {
        email: req.query.email,
      },
    });
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!user) {
    return res.status(404).json({ Erro: "Usuário não encontrado." });
  } else {
    user = Object.assign({}, user[0].dataValues);
    delete user.password;
    return res.send(user);
  }
};

exports.create = async (req, res) => {
  const payload = req.body;
  let user = null;

  if (!payload) {
    return res.status(400).json({
      Erro: "Requisição inválida.",
    });
  }

  payload.password = await bcrypt.hash(payload.password, 10);

  try {
    user = await User.create(payload);
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!user) {
    return res
      .status(400)
      .json({ Erro: "Não foi possível cadastrar o usuário." });
  } else {
    return res.send(user);
  }
};

exports.updateById = async (req, res) => {
  const paramsId = req.params.id;
  const payload = req.body;
  let user = null;

  try {
    user = await User.update(payload, {
      where: {
        id: paramsId,
      },
      returning: true,
    });

    user = user[1][0];
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!user) {
    return res.status(404).json({ Erro: "Usuário não encontrado." });
  } else {
    user = Object.assign({}, user.dataValues);
    delete user.password;
    return res.send(user);
  }
};

exports.deleteById = async (req, res) => {
  const paramsId = req.params.id;
  let user = null;

  try {
    user = await User.destroy({
      where: {
        id: paramsId,
      },
    });
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!user) {
    return res.status(404).json({ Erro: "Usuário não encontrado." });
  } else {
    return res.json({ Message: "Usuário removido." });
  }
};

exports.validateLogin = async (req, res) => {
  let user = null;

  if (!req.body && !req.body.email && !req.body.password) {
    return res.status(401).json({ Erro: "Usuário ou senha inválidos." });
  }

  try {
    user = await User.findAll({
      where: {
        email: req.body.email,
      },
    });
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  const isValid = await bcrypt.compare(req.body.password, user.password);

  if (!user && !isValid) {
    return res.status(401).json({ Erro: "E-mail ou senha inválidos." });
  } else {
    const token = jwt.sign({ id: user.id }, "s3cret2023", { expiresIn: "2h" });

    return res.status(200).json({ token: token });
  }
};
