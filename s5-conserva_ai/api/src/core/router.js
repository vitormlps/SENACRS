// Local imports
const app = require("./app");
// const authentication = require("../middleware/authentication");
const loginRoute = require("../routes/loginRoute");
const usersRoute = require("../routes/usersRoute");
const transactionsRoute = require("../routes/transactionsRoute");
const productsRoute = require("../routes/productsRoute");
const batchesRoute = require("../routes/batchesRoute");
const categoriesRoute = require("../routes/categoriesRoute");

app.use("/api/login", loginRoute);

// app.use("/api/users", authentication.validateToken("user"), usersRoute);
app.use("/api/users", usersRoute);

app.use("/api/transactions", transactionsRoute);

// app.use('/api/inventory', authentication.validateToken, routeInventory);
app.use("/api/products", productsRoute);

app.use("/api/batches", batchesRoute);

app.use("/api/categories", categoriesRoute);

module.exports = app;
