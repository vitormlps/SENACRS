// Third-party imports
const bcrypt = require("bcrypt");

// Local imports
const User = require("../database/models/user");
const Product = require("../database/models/product");
const Batch = require("../database/models/batch");
const Category = require("../database/models/category");

const addUsers = () => {
  const users = [
    {
      name: "John Doe",
      email: "john.doe@gmail.com",
      password: "123456",
    },
    {
      name: "Maria Silva",
      email: "maria.silva@hotmail.com",
      password: "123456",
    },
    {
      name: "João Garcias",
      email: "joao.garcias@conserva.ai",
      password: "123456",
    },
  ];

  users.forEach(async (user) => {
    user.password = await bcrypt.hash(user.password, 10);
    await User.create(user);
  });
};

const addProducts = () => {
  const products = [
    {
      name: "Uva",
      description: "",
      minQty: 0,
      maxQty: 20,
      measurementUnit: "g",
    },
    {
      name: "Carne",
      description: "",
      minQty: 5,
      maxQty: 50,
      measurementUnit: "kg",
    },
    {
      name: "Leite",
      description: "",
      minQty: 10,
      maxQty: 100,
      measurementUnit: "ml",
    },
  ];

  products.forEach((product) => {
    Product.create(product);
  });
};

const addBatches = () => {
  const batches = [
    {
      expirationDate: "2023-12-01",
      quantity: 21,
      location: "Armazem 1",
      productId: 1,
      userId: 1,
    },
    {
      expirationDate: "2024-01-01",
      quantity: 10,
      location: "Armazem 2",
      productId: 2,
      userId: 2,
    },
    {
      expirationDate: "2023-11-01",
      quantity: 7,
      location: "Armazem 3",
      productId: 3,
      userId: 3,
    },
  ];

  batches.forEach((batch) => {
    Batch.create(batch);
  });
};

const addCategories = () => {
  const categories = [
    {
      name: "Frutas",
    },
    {
      name: "carnes",
    },
    {
      name: "Lácteos",
    },
  ];

  categories.forEach((category) => {
    Category.create(category);
  });
};

exports.populateDatabase = () => {
  addUsers();
  addProducts();
  addBatches();
  addCategories();
};
