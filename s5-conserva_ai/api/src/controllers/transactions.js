// Local imports
const Transaction = require("../database/models/transaction");

exports.findAll = async (req, res) => {
  let transactions = [];

  try {
    transactions = await Transaction.findAll();
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (transactions.length == 0) {
    return res.status(404).json({ Erro: "Não há transações cadastradas." });
  } else {
    return res.send(transactions);
  }
};

exports.findById = async (req, res) => {
  const paramsId = req.params.id;
  let transaction = null;

  try {
    transaction = await Transaction.findByPk(paramsId);
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!transaction) {
    return res.status(404).json({ Erro: "Transação não encontrada." });
  } else {
    return res.send(transaction);
  }
};

exports.create = async (payload) => {
  let transaction = null;

  try {
    transaction = await Transaction.create(payload);
  } catch (err) {
    console.log("Erro:", err);
    return;
  }

  if (!transaction) {
    console.log("Erro: Não foi possível cadastrar a transação.");
    return;
  } else {
    console.log("Transação salva.");
    return;
  }
};
