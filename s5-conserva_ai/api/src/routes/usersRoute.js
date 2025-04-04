// Third-party imports
const express = require("express");

// Local imports
const usersController = require("../controllers/users");

const router = express.Router();

router.get("/", usersController.findAll);
router.get("/get", usersController.findByEmail);
router.get("/:id", usersController.findById);

router.post("/", usersController.create);

router.put("/:id", usersController.updateById);

router.delete("/:id", usersController.deleteById);

module.exports = router;
