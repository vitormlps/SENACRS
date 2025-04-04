// Third-party imports
const { DataTypes, Model } = require("sequelize");

// Local imports
const { sequelize } = require("../connect");

class Transaction extends Model {}

Transaction.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    datetime: {
      type: DataTypes.DATE,
      allowNull: false,
      defaultValue: DataTypes.NOW,
      validate: {
        isDate: true,
      },
    },
    type: {
      type: DataTypes.STRING(6),
      allowNull: false,
      validate: {
        isAlpha: true,
        isUppercase: true,
        len: [3, 6],
      },
    },
    entity: {
      type: DataTypes.STRING(20),
      allowNull: false,
      validate: {
        isAlpha: true,
        isUppercase: true,
        len: [4, 20],
      },
    },
    field: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    value: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
    userName: {
      type: DataTypes.STRING(100),
      allowNull: false,
      validate: {
        // isAlpha: true,
        notEmpty: true,
        len: [2, 100],
      },
    },
  },
  {
    sequelize,
    tableName: "transactions",
    defaultScope: {
      order: ["datetime", "DESC"],
    },
  }
);

Transaction.sync({ alter: true });

module.exports = Transaction;
