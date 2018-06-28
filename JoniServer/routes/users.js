var express = require('express');
var router = express.Router();

var usersController = require('../controllers/usersController.js');

/* GET all users  */
router.get('/', function(req, res, next) {
    usersController.index(req,res);
});

/* UPDATE user preferred categories  */
router.post('/', function(req, res, next) {
    usersController.updateUserCategories(req,res);
});

module.exports = router;
