// Third-party imports
const dotenv = require("dotenv");

dotenv.config();

module.exports = {
  PORT: process.env.PORT,
  DATABASE_URI: process.env.DATABASE_URI,
};
