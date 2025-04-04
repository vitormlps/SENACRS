// Local imports
const Batch = require("../database/models/batch");
const CategoryBatches = require("../database/models/categoryBatches");
const transactionsController = require("../controllers/transactions");

exports.findAll = async (req, res) => {
  let batches = [];

  if (req.query?.productId) {
    try {
      batches = await Batch.findAll({
        where: {
          productId: req.query.productId,
        },
      });
    } catch (err) {
      return res.status(500).json({ Erro: err });
    }
  } else {
    try {
      batches = await Batch.findAll();
    } catch (err) {
      return res.status(500).json({ Erro: err });
    }
  }

  if (batches.length == 0) {
    return res.status(404).json({ Erro: "Não há lotes cadastrados." });
  } else {
    return res.send(batches);
  }
};

exports.findById = async (req, res) => {
  const paramsId = req.params.id;
  let batch = null;

  try {
    batch = await Batch.findByPk(paramsId);
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!batch) {
    return res.status(404).json({ Erro: "Lote não encontrado." });
  } else {
    return res.send(batch);
  }
};

// function validatePayload(payload) {
//   Object.values(payload).forEach((value) => {
//     if (value) {
//     }
//   });
// }

exports.create = async (req, res) => {
  const payload = req.body;
  let batch = null;

  //   const isValid = validatePayload(payload);

  if (!payload) {
    return res.status(400).json({
      Erro: "Requisição inválida.",
    });
  }

  try {
    batch = await Batch.create(payload);
    await transactionsController.create({
      type: "POST",
      entity: "BATCH",
      prevValue: payload.prevQuantity,
      nextValue: batch.quantity,
      userId: payload.userId,
    });
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!batch) {
    return res.status(400).json({ Erro: "Não foi possível cadastrar o lote." });
  } else {
    return res.send(batch);
  }
};

exports.updateById = async (req, res) => {
  const paramsId = req.params.id;
  const payload = req.body;
  let batch = null;

  try {
    batch = await Batch.update(payload, {
      where: {
        id: paramsId,
      },
      returning: true,
    });
    await transactionsController.create({
      type: "UPDATE",
      entity: "BATCH",
      prevValue: payload.prevQuantity,
      nextValue: batch.quantity,
      userId: payload.userId,
    });
    batch = batch[1][0];
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!batch) {
    return res.status(404).json({ Erro: "Lote não encontrado." });
  } else {
    return res.send(batch);
  }
};

exports.deleteById = async (req, res) => {
  const paramsId = req.params.id;
  let batch = null;

  try {
    batch = await Batch.destroy({
      where: {
        id: paramsId,
      },
    });
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!batch) {
    return res.status(404).json({ Erro: "Lote não encontrado." });
  } else {
    return res.json({ Message: "Lote removido." });
  }
};

exports.categorize = async (req, res) => {
  const payload = req.body;
  let categoryBatch = null;

  if (!payload || (!payload.batchId && !payload.categoryId)) {
    return res.status(400).json({
      Erro: "Requisição inválida.",
    });
  }

  try {
    categoryBatch = await CategoryBatches.create(payload);
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!categoryBatch) {
    return res
      .status(400)
      .json({ Erro: "Não foi possível categorizar o lote." });
  } else {
    return res.send(categoryBatch);
  }
};

exports.decategorize = async (req, res) => {
  const payload = req.body;
  let categoryBatch = null;

  if (!payload || (!payload.batchId && !payload.categoryId)) {
    return res.status(400).json({
      Erro: "Requisição inválida.",
    });
  }

  try {
    categoryBatch = await CategoryBatches.destroy({
      where: {
        batchId: payload.batchId,
        categoryId: payload.categoryId,
      },
    });
  } catch (err) {
    return res.status(500).json({ Erro: err });
  }

  if (!categoryBatch) {
    return res
      .status(400)
      .json({ Erro: "Não foi possível descategorizar o lote." });
  } else {
    return res.json({ Message: "Categoria removida do lote." });
  }
};

// exports.updateBatchQty = async (req, res) => {
//   const payload = req.body;
//   const batches = [];

//   try {
//     for (const item of itemsToUpdate) {
//       const { _id, quantity } = item;

//       await Batch.increment({quantity: 5}, { where: { id: payload.id } })

//       const updatedItem = await Inventory.findByIdAndUpdate(
//         _id,
//         { quantity },
//         { new: true }
//       );

//       if (updatedItem) {
//         updatedItems.push(updatedItem);
//       }
//     }
//   } catch (err) {
//     return res.status(500).json({ Error: err });
//   }

//   if (batches.length == 0) {
//     return res.status(404).json({ Erro: "Não há lotes cadastrados." });
//   } else {
//     return res.send(batches);
//   }
// };
