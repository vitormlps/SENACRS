// Third-party imports
const express = require("express");

// Local imports
const categoriesController = require("../controllers/categories");

const router = express.Router();

router.get("/", categoriesController.findAll);
router.get("/:id", categoriesController.findById);

router.post("/", categoriesController.create);

router.put("/:id", categoriesController.updateById);

router.delete("/:id", categoriesController.deleteById);

module.exports = router;
