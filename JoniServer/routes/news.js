var express = require('express');
var router = express.Router();

var newsController = require('../controllers/newsController.js');

/* GET all news */
router.get('/', function(req, res, next) {
    newsController.getAllNews(req,res);
});

/* GET updated news from NewsAPI */
router.get('/update', function(req, res, next) {
    newsController.update(req,res);
});

/* GET latest news titles by category  */
router.get('/:userId/:category/latest', function(req, res, next) {
    newsController.getNewsTitlesByCategory(req,res);
});

/* GET news title audio  */
router.get('/:userId/:newsId/title', function(req, res, next) {
    newsController.getNewsTitleAudioByNewsId(req,res);
});

/* GET news found by its id  */
router.get('/:userId/:newsId', function(req, res, next) {
    newsController.getNewsById(req,res);
});

/* GET news description audio  */
router.get('/:userId/:newsId/description', function(req, res, next) {
    newsController.getNewsDescriptionAudioByNewsId(req,res);
});


module.exports = router;
