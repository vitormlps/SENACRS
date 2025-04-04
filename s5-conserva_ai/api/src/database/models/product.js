// Third-party imports
const { DataTypes, Model, Deferrable } = require("sequelize");

// Local imports
const { sequelize } = require("../connect");
// const Batch = require("./batch");
// const Category = require("./category");

class Product extends Model {
  // static classLevelMethod() {
  //     return 'foo';
  //   }
  //   instanceLevelMethod() {
  //     return 'bar';
  //   }
  //   getFullname() {
  //     return [this.firstname, this.lastname].join(' ');
  //   }
}

Product.init(
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
        len: [2, 100],
      },
    },
    description: {
      type: DataTypes.TEXT("medium"),
      allowNull: false,
      defaultValue: "",
    },
    minQty: {
      type: DataTypes.INTEGER,
      allowNull: false,
      defaultValue: 0,
      validate: {
        isInt: true,
        max: 999,
        min: 0,
      },
    },
    maxQty: {
      type: DataTypes.INTEGER,
      allowNull: false,
      defaultValue: 999,
      validate: {
        isInt: true,
        max: 999,
        min: 1,
      },
    },
    measurementUnit: {
      type: DataTypes.STRING(30),
      allowNull: false,
      defaultValue: "g",
      validate: {
        len: [1, 30],
      },
    },
  },
  {
    sequelize,
    tableName: "products",
    // include: [
    //   {
    //     association: Product.User,
    //     include: [User.Addresses],
    //   },
    // ],
    // defaultScope: {
    //   where: {
    //     active: true,
    //   },
    // },
  }
);

Product.sync({ alter: true });

module.exports = Product;
