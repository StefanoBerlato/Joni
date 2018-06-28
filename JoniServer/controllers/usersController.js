var categoriesDA = require('../dataAccess/categoriesDA.js');
var usersDA = require('../dataAccess/usersDA.js');

var Category = require('../models/category.js');
var User = require('../models/user.js');


function index(req,res){
  res.json(usersDA.getAllUsers());
}

function updateUserCategories(req,res){

    var newPrefCategories = req.body.categories;
    // console.log("userId: "+req.body.userId);
    var findUser = usersDA.getUserById(new User(req.body.userId));
    // console.log("findUser: "+findUser);
    // console.log("categories: "+typeof newPrefCategories);

    if (findUser !== undefined){
      var updatedCategories = usersDA.updateUserCategories(findUser,newPrefCategories);
    }

    if (!updatedCategories) {
      res.json("Errore");
    } else {
      res.json(findUser);
    }
}

exports.index = index;
exports.updateUserCategories = updateUserCategories;
