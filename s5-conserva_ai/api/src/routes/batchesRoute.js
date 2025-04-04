// Third-party imports
const express = require("express");

// Local imports
const batchesController = require("../controllers/batches");

const router = express.Router();

router.get("/", batchesController.findAll);
router.get("/:id", batchesController.findById);

router.post("/", batchesController.create);
router.post("/categories", batchesController.categorize);

router.put("/:id", batchesController.updateById);

router.delete("/categories", batchesController.decategorize);
router.delete("/:id", batchesController.deleteById);

// router.patch(':id/update-items-quantity', batchesController.updateItemsQuantity);

module.exports = router;
