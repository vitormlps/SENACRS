// Local imports
const config = require("./core/config");
const app = require("./core/router"); // O app passa pelo router antes de iniciar
const { testDbConnection } = require("./database/connect");
const { populateDatabase } = require("./utils/populate_db");

testDbConnection();

// populateDatabase();

app.listen(config.PORT, () => {
  console.log(`Servidor iniciado na porta ${config.PORT}`);
});
