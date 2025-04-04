// Third-party imports
const { DataTypes, Model } = require("sequelize");

// Local imports
const { sequelize } = require("../connect");
// const Transaction = require("./transaction");

class User extends Model {}

User.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    name: {
      type: DataTypes.STRING(100),
      allowNull: false,
      validate: {
        // isAlpha: true,
        notEmpty: true,
        len: [2, 100],
      },
    },
    email: {
      type: DataTypes.STRING(50),
      allowNull: false,
      unique: true,
      validate: {
        isEmail: true,
        notEmpty: true,
        len: [5, 50],
      },
    },
    password: {
      type: DataTypes.STRING(64),
      validate: {
        // is: /^[0-9a-f]{64}$/i,
        notEmpty: true,
        len: [6, 64],
      },
      allowNull: false,
    },
  },
  {
    sequelize,
    tableName: "users",
  }
);

// User.hasMany(Transaction);

User.sync({ alter: true });

module.exports = User;
