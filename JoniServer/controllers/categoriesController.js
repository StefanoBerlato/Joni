var newsDA = require('../dataAccess/newsDA.js');
var categoriesDA = require('../dataAccess/categoriesDA.js');
var usersDA = require('../dataAccess/usersDA.js');

var News = require('../models/news.js');
var Category = require('../models/category.js');
var User = require('../models/user.js');


// To query sources
// All options are optional
function index (req,res){
  var response = categoriesDA.getAllCategories();
  res.json(response);
}


function getCategoriesByUser (req,res){
  var userId = req.params.userId;
  var fetchingUser = new User (userId);
  var user = usersDA.getUserById(fetchingUser);
  var result = [];

  result = user.categories;
  res.json(result);
}

function getCategoryAudio (req,res){
  var category = new Category(req.params.category);

  var catTmp = categoriesDA.getCategoryByName(category);

  res.download(catTmp.nameAudioPath)


}



exports.index = index;
exports.getCategoriesByUser = getCategoriesByUser;
exports.getCategoryAudio = getCategoryAudio;
