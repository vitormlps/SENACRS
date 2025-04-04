// Third-party imports
const express = require("express");

// Local imports
const productsController = require("../controllers/products");

const router = express.Router();

router.get("/", productsController.findAll);
router.get("/:id", productsController.findById);

router.post("/", productsController.create);
router.post("/categories", productsController.categorize);

router.put("/:id", productsController.updateById);

router.delete("/categories", productsController.decategorize);
router.delete("/:id", productsController.deleteById);

module.exports = router;
