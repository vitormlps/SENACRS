// Third-party imports
const express = require("express");

// Local imports
const transactionsController = require("../controllers/transactions");

const router = express.Router();

router.get("/", transactionsController.findAll);
router.get("/:id", transactionsController.findById);

// router.post("/", transactionsController.create);

module.exports = router;
