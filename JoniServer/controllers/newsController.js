var newsDA = require('../dataAccess/newsDA.js');
var categoriesDA = require('../dataAccess/categoriesDA.js');
var usersDA = require('../dataAccess/usersDA.js');

var News = require('../models/news.js');
var Category = require('../models/category.js');
var User = require('../models/user.js');

var fs = require('fs');


async function update (req,res){
  try {
    console.log("Downoading news...");
    await newsDA.updateNews();
  } catch (e) {
    console.log(e);
  } finally {
    res.json("news updated");
  }
}

function getAllNews (req,res){
  var result = newsDA.getAllNews();

  res.json(result);
}


//fetch news titles by chosen category
function getNewsTitlesByCategory (req,res){
  var userId = req.params.userId;
  var category = categoriesDA.getCategoryByName(new Category(req.params.category));
  var fetchingUser = new User (userId);
  var user = usersDA.getUserById(fetchingUser);

  var result = [];

  // fake authentication
  if (user !== null) {
    result = newsDA.getNewsTitlesByCategory(category);
  }

  res.json(result);
}

async function getNewsTitleAudioByNewsId (req, res){
  var newsId = req.params.newsId;

  var findNews = new News();
  findNews.newsId = newsId;

  // fake authentication

    let newsTmp;
    try {
      newsTmp = await newsDA.getNewsTitleAudioByNewsId(findNews);
    } catch (e) {
      console.log(e);
    }

    res.download(newsTmp.titleAudioPath);

    // var stat;
    // if (newsTmp != undefined) {
    //   try{
    //     stat = fs.statSync(""+newsTmp.titleAudioPath);
    //   } catch (e) {
    //     console.log(e);
    //   }
    //
    //   res.writeHead(200, {
    //       'Content-Type': 'audio/mpeg',
    //       'Content-Length': stat.size
    //   });
    //   fs.createReadStream(""+newsTmp.titleAudioPath).pipe(res);
    //
    // } else {
    //   res.json("Not found");
    // }




}


function getNewsById (req,res){
  var userId = req.params.userId;
  var newsId = req.params.newsId;

  var fetchingUser = new User (userId);
  var user = usersDA.getUserById(fetchingUser);

  var findNews = new News();
  findNews.newsId = newsId;

  var result;

  // fake authentication
  if (user !== null) {
    result = newsDA.getNewsById(findNews);
  }

  res.json(result);
}

async function getNewsDescriptionAudioByNewsId(req,res){
  var newsId = req.params.newsId;

  var findNews = new News();
  findNews.newsId = newsId;

  let newsTmp;
  try {
    newsTmp = await newsDA.getNewsDescriptionAudioByNewsId(findNews);
  } catch (e) {
    console.log(e);
  }

  var stat;
  if (newsTmp != undefined) {

    res.download(newsTmp.descritpionAudioPath);

  } else {
    res.json("Not found");
  }
}



exports.getNewsTitlesByCategory = getNewsTitlesByCategory;
exports.getNewsTitleAudioByNewsId = getNewsTitleAudioByNewsId;
exports.getNewsById = getNewsById;
exports.getNewsDescriptionAudioByNewsId = getNewsDescriptionAudioByNewsId;
exports.getAllNews = getAllNews;
exports.update = update;
