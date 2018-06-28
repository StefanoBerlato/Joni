var express = require('express');
var router = express.Router();

var categoriesController = require('../controllers/categoriesController.js');

/* GET all categories */
router.get('/', function(req, res, next) {
    categoriesController.index(req,res);
});

/* GET all categories by userId */
router.get('/:userId', function(req, res, next) {
    categoriesController.getCategoriesByUser(req,res);
});

/* GET category audio */
router.get('/:category/audio', function(req, res, next) {
    categoriesController.getCategoryAudio(req,res);
});

module.exports = router;
