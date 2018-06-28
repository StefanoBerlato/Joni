var user = require('../models/user.js');
var Category = require('../models/category.js');

var categoryDA = require('../dataAccess/categoriesDA.js');

var users = [];

/**
 * This function checks if the user's Id is correct
 * @param user
 * @return res if the name is correct or not
 **/
function validateId (user) {
  res = false;
  var error;

  if (user.id === '') {
    error = "Id is empty";
    user.errors.push(error);
  }
  if (user.id === undefined) {
    error = "Id is undefined";
    user.errors.push(error);
  }
  if (user.errors.length === 0) {
    res = true;
  }

  return res;
}

/**
 * This function checks if the user's Name is correct
 * @param user
 * @return res if the name is correct or not
 **/
function validateName (user) {
  res = false;
  var error;

  if (user.name === '') {
    error = "Name is empty";
    user.errors.push(error);
  }
  if (user.name === undefined) {
    error = "Name is undefined";
    user.errors.push(error);
  }
  if (user.errors.length === 0) {
    res = true;
  }

  return res;
}

/**
 * This function checks if the user's Surname is correct
 * @param user
 * @return res if the name is correct or not
 **/
function validateSurname (user) {
  res = false;
  var error;

  if (user.surname === '') {
    error = "Surname is empty";
    user.errors.push(error);
  }
  if (user.surname === undefined) {
    error = "Surname is undefined";
    user.errors.push(error);
  }
  if (user.errors.length === 0) {
    res = true;
  }

  return res;
}

/**
 * This function checks if the user's Email is correct
 * @param user
 * @return res if the name is correct or not
 **/
function validateEmail (user) {
  res = false;
  var error;

  if (user.email === '') {
    error = "Email is empty";
    user.errors.push(error);
  }
  if (user.email === undefined) {
    error = "Email is undefined";
    user.errors.push(error);
  }
  if (user.errors.length === 0) {
    res = true;
  }

  return res;
}

/**
 * This function checks if the user's Categories is correct
 * @param user
 * @return res if the name is correct or not
 **/
function validateCategories (user) {
  res = false;
  var error;

  for (var i = 0; i < user.categories.length; i++) {
    if (!(categoryDA.isValid(user.categories[i]))) {
      error = "Categories are not valid";
      user.errors.push(error);
    }
  }

  if (user.errors.length === 0) {
    res = true;
  }

  return res;
}

/**
 * This function checks if the user object is valid
 * @param user
 * @return res if the user has passed all validation tests
 **/
function isValid (user) {
  var res = true;

  if (!validateId(user)){
    res = false;
  }
  if (!validateName(user)){
    res = false;
  }
  if (!validateSurname(user)){
    res = false;
  }
  if (!validateEmail(user)){
    res = false;
  }
  if (!validateCategories(user)){
    res = false;
  }
  return res;
}

/**
 * This function tries to add a user
 * It first checks if the parameter is valid and then if it does already exist.
 * If not, it then adds the new user
 * @param user the new user to be added
 * @return res if the user has been added or not
 **/
function addUser(user) {
  var res = false;
  if (isValid(user)){

      users.push(user);
      res = true;

  }

  return res;
}

/**
 * This function return all users stored
 * @return res users list
 **/
function getAllUsers () {
  return users;
}

/**
 * This function returns a user by the specified name
 * @param user the name to find
 * @return res if the user found or not
 **/
function getUserByName(user){
  var res = false;
  for (var i = 0; i < users.length; i++) {
    if (users[i].Name === user.Name){
      res = users[i];
    }
  }
  return res;
}

/**
 * This function returns a user by the specified name
 * @param user the name to find
 * @return res if the user found or not
 **/
function getUserById(user){
  var res;

  for (var i = 0; i < users.length; i++) {
    if (users[i].id === user.id){
      res = users[i];
    }
  }

  return res;
}

function updateUserCategories(user, newCategories){
  res = false;
  var foundUser = getUserById(user);
  if (foundUser !== undefined) {
    foundUser.categories = [];
    for (var i = 0; i < newCategories.length; i++) {
      var tmp = new Category(newCategories[i]);
      foundUser.categories.push(categoryDA.getCategoryByName(tmp));
    }
    res = true
  }
  return res;
}

function cleanUsers () {
  users = [];
}

exports.isValid = isValid;
exports.addUser = addUser;
exports.getAllUsers = getAllUsers;
exports.getUserByName = getUserByName;
exports.getUserById = getUserById;
exports.cleanUsers = cleanUsers;
exports.updateUserCategories = updateUserCategories;

//DEFAULT VALUES
// business entertainment general health science sports technology
var user_default_1 = new user("1", "Mario", "Rossi", "mario@rossi.me");
var user_category_1 = new Category("business","/Users/giovanni/Dropbox/Uni/EIT/ICTInn/Joni/Server/recordings/business/name/business.mp3");
var user_category_2 = new Category("entertainment","/Users/giovanni/Dropbox/Uni/EIT/ICTInn/Joni/Server/recordings/business/name/entertainment.mp3");
var user_category_3 = new Category("technology","/Users/giovanni/Dropbox/Uni/EIT/ICTInn/Joni/Server/recordings/technology/name/technology.mp3");
var user_category_4 = new Category("general","/Users/giovanni/Dropbox/Uni/EIT/ICTInn/Joni/Server/recordings/technology/name/general.mp3");
var user_category_5 = new Category("health","/Users/giovanni/Dropbox/Uni/EIT/ICTInn/Joni/Server/recordings/technology/name/health.mp3");
var user_category_6 = new Category("science","/Users/giovanni/Dropbox/Uni/EIT/ICTInn/Joni/Server/recordings/technology/name/science.mp3");
var user_category_7 = new Category("sports","/Users/giovanni/Dropbox/Uni/EIT/ICTInn/Joni/Server/recordings/technology/name/sports.mp3");


user_default_1.categories.push(user_category_1);
user_default_1.categories.push(user_category_2);
user_default_1.categories.push(user_category_3);
user_default_1.categories.push(user_category_4);
user_default_1.categories.push(user_category_5);
user_default_1.categories.push(user_category_6);
user_default_1.categories.push(user_category_7);

addUser(user_default_1);
