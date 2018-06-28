var category = require('../models/category.js');

var Category = require('../models/category.js');

var tts = require('../utils/tts.js');

var newsLanguage = 'it';

var categories = [];

/**
 * This function checks if the category'Name is correct
 * @param category
 * @return res if the name is correct or not
 **/
function validateName (category) {
  res = false;
  var error;

  if (category.name === '') {
    error = "Name is empty";
    category.errors.push(error);
  }
  if (category.name === undefined) {
    error = "Name is undefined";
    category.errors.push(error);
  }
  if (category.errors.length === 0) {
    res = true;
  }

  return res;
}

/**
 * This function checks if the category object is valid
 * @param category
 * @return res if the category has passed all validation tests
 **/
function isValid (category) {
  var res = true;
  if (!validateName(category)){
    res = false;
  }
  return res;
}

/**
 * This function tries to add a category
 * It first checks if the parameter is valid and then if it does already exist.
 * If not, it then adds the new category
 * @param category the new category to be added
 * @return res if the category has been added or not
 **/
async function addCategory(category) {
  var res = false;
  // if (isValid(category)){
    // if (categories.length <= 0 || !getCategoryByName(category)){

      category.nameAudioPath = await tts.tts(category.name, "name", category.name, newsLanguage);
      categories.push(category);
      res = true;
    // }
  // }

  return res;
}

/**
 * This function return all categories stored
 * @return res categories list
 **/
function getAllCategories () {
  return categories;
}

/**
 * This function returns a category by the specified name
 * @param category the name to find
 * @return res if the category found or not
 **/
function getCategoryByName(category){
  var res;
  for (var i = 0; i < categories.length; i++) {
    if (categories[i].name === category.name){
      res = categories[i];
    }
  }
  return res;
}

function cleanCategories () {
  categories = [];
}

exports.isValid = isValid;
exports.addCategory = addCategory;
exports.getAllCategories = getAllCategories;
exports.getCategoryByName = getCategoryByName;
exports.cleanCategories = cleanCategories;

//DEFAULT VALUES
// business entertainment general health science sports technology
var category_default_1 = new Category("business");
var category_default_2 = new Category("entertainment");
var category_default_3 = new Category("general");
var category_default_4 = new Category("health");
var category_default_5 = new Category("science");
var category_default_6 = new Category("sports");
var category_default_7 = new Category("technology");

addCategory(category_default_1);
addCategory(category_default_2);
addCategory(category_default_3);
addCategory(category_default_4);
addCategory(category_default_5);
addCategory(category_default_6);
addCategory(category_default_7);
