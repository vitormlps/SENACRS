const logger = (req, res, next) => {
  console.log("[REQUEST]", `${req.method} ${req.originalUrl}`);
  next();
  console.log("[RESPONSE]", `${res.statusCode}`);
};

module.exports = logger;
