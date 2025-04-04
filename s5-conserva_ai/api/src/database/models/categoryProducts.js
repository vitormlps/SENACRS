// Third-party imports
const { DataTypes, Model, Deferrable } = require("sequelize");

// Local imports
const { sequelize } = require("../connect");
const Product = require("./product");
const Category = require("./category");

class CategoryProducts extends Model {}

CategoryProducts.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    productId: {
      type: DataTypes.INTEGER,
      references: {
        model: Product,
        key: "id",
        deferrable: Deferrable.INITIALLY_IMMEDIATE,
      },
    },
    categoryId: {
      type: DataTypes.INTEGER,
      references: {
        model: Category,
        key: "id",
        deferrable: Deferrable.INITIALLY_IMMEDIATE,
      },
    },
  },
  {
    sequelize,
    tableName: "category_products",
  }
);

CategoryProducts.sync({ alter: true });

module.exports = CategoryProducts;
