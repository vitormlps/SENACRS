// Third-party imports
const { DataTypes, Model } = require("sequelize");

// Local imports
const { sequelize } = require("../connect");
// const Batch = require("./batch");
// const Product = require("./product");

class Category extends Model {}

Category.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    name: {
      type: DataTypes.STRING(30),
      allowNull: false,
      unique: true,
      validate: {
        notEmpty: true,
        len: [1, 30],
      },
    },
  },
  {
    sequelize,
    tableName: "categories",
  }
);

// Category.belongsToMany(Product, { through: "CategoryProducts" });
// Category.belongsToMany(Batch, { through: "CategoryBatches" });

Category.sync({ alter: true });

module.exports = Category;
