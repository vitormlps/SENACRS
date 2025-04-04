// Third-party imports
const { Sequelize } = require("sequelize");

// Local imports
const config = require("../core/config");

const sequelize = new Sequelize(config.DATABASE_URI);

const testDbConnection = async () => {
  try {
    await sequelize.authenticate();
    console.log("Connection has been established successfully.");
  } catch (error) {
    console.warn("Unable to connect to the database:", error);
  }
};

module.exports = { sequelize, testDbConnection };
