// Third-party imports
const { DataTypes, Model, Deferrable } = require("sequelize");

// Local imports
const { sequelize } = require("../connect");
const Product = require("./product");
const { getDateNow } = require("../../utils/get_date");
// const Category = require("./category");

class Batch extends Model {}

Batch.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    expirationDate: {
      type: DataTypes.DATE,
      allowNull: false,
      defaultValue: DataTypes.NOW,
      validate: {
        isDate: true,
        isAfter: getDateNow(),
      },
    },
    quantity: {
      type: DataTypes.INTEGER,
      allowNull: false,
      defaultValue: 1,
      validate: {
        isInt: true,
        max: 999,
        min: 1,
      },
    },
    location: {
      type: DataTypes.STRING(100),
      allowNull: true,
      validate: {
        notEmpty: true,
      },
    },
    productId: {
      type: DataTypes.INTEGER,
      references: {
        model: Product,
        key: "id",
        deferrable: Deferrable.INITIALLY_IMMEDIATE,
      },
    },
  },
  {
    sequelize,
    tableName: "batches",
  }
);

// Batch.belongsTo(Product);
// Batch.hasMany(Category);

Batch.sync({ alter: true });

module.exports = Batch;
