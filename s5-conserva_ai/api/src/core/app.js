// Third-party imports
const express = require("express");

// Local imports
const cors = require("../middleware/cors");
// const authentication = require("../middleware/authentication");
const logger = require("../middleware/logger");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(cors);

// app.use(authentication);
// app.use(authentication.validateToken);

app.use(logger);

module.exports = app;
