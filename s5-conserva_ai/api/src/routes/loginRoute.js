// Third-party imports
const express = require("express");

// Local imports
const usersController = require("../controllers/users");

const router = express.Router();

router.post("/", usersController.validateLogin);

module.exports = router;
