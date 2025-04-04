// Third-party imports
const { DataTypes, Model, Deferrable } = require("sequelize");

// Local imports
const { sequelize } = require("../connect");
const Batch = require("./batch");
const Category = require("./category");

class CategoryBatches extends Model {}

CategoryBatches.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    batchId: {
      type: DataTypes.INTEGER,
      references: {
        model: Batch,
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
    tableName: "category_batches",
  }
);

CategoryBatches.sync({ alter: true });

module.exports = CategoryBatches;
