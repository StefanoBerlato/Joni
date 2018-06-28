var News = require('../models/news.js');
var Category = require('../models/category.js');
var categoryDA = require('../dataAccess/categoriesDA.js');
var schedule = require('node-schedule');

// Const variables
const TOKEN = "";
const NewsAPI = require('newsapi');
const newsapi = new NewsAPI(TOKEN);

const newsLanguage = 'it';
const newsCountry = 'it';

var endText = ". News terminata. Premi avanti per leggere gli altri titoli."

var tts = require('../utils/tts.js');

var newsList = [];

function ID () {
  // Math.random should be unique because of its seeding algorithm.
  // Convert it to base 36 (numbers + letters), and grab the first 9 characters
  // after the decimal.
  return '_' + Math.random().toString(36).substr(2, 9);
};


/**
* This function checks if the news's Name is correct
* @param news
* @return res if the name is correct or not
**/
function validateTitle (news) {
  res = false;
  var error;

  if (news.title === '') {
    error = "Name is empty";
    news.errors.push(error);
  }
  if (news.title === null) {
    error = "Name is empty";
    news.errors.push(error);
  }
  if (news.title === undefined) {
    error = "Name is undefined";
    news.errors.push(error);
  }
  if (news.errors.length === 0) {
    res = true;
  }
  //
  return res;
}

/**
* This function checks if the news's Description is correct
* @param news
* @return res if the name is correct or not
**/
function validateDescription (news) {
  res = false;
  var error;

  if (news.description === '') {
    error = "Description is empty";
    news.errors.push(error);
  }
  if (news.description === null) {
    error = "Description is empty";
    news.errors.push(error);
  }
  if (news.description === undefined) {
    error = "Description is undefined";
    news.errors.push(error);
  }
  if (news.errors.length === 0) {
    res = true;
  }

  return res;
}


/**
* This function checks if the news object is valid
* @param news
* @return res if the news has passed all validation tests
**/
function isValid (news) {
  var res = true;

  if (!validateTitle(news)){
    res = false;
  }
  if (!validateDescription(news)){
    res = false;
  }


  return res;
}


function updateNews(){
  var result = false;
  var storedCategories = categoryDA.getAllCategories();

  cleanNews();

  return storedCategories.forEach(function(listItem, index){
    newsapi.v2.topHeadlines({
      // sources: 'bbc-news,the-verge',
      // q: 'bitcoin',
      category: listItem.name,
      //language: newsLanguage,
      country: newsCountry
    }).then(response => {
      if (response.status === "ok"){
        for (var i=0; i < response.articles.length; i++){
          var newNews = new News();
          newNews.newsId = ID();
          // newNews.sourceId = response.articles[i].source.id;
          // newNews.sourceName = response.articles[i].source.name;
          // newNews.author = response.articles[i].author;
          newNews.title = response.articles[i].title;
          newNews.description = response.articles[i].description;
          // newNews.url = response.articles[i].url;
          // newNews.urlToImage = response.articles[i].urlToImage;
          // newNews.publishedAt = response.articles[i].publishedAt;
          newNews.category = listItem;

          if (isValid(newNews)){
            newNews.description = newNews.description+endText;
            newsList.push(newNews);
          }
        }
      }
    }).catch("Error while downloding from NewsAPI");
  });

}


/**
* This function tries to add a news
* It first checks if the parameter is valid and then if it does already exist.
* If not, it then adds the new news
* @param news the new news to be added
* @return res if the news has been added or not
**/
function addNews(news) {
  var res = false;
  // if (isValid(news)){
  newsList.push(news);
  res = true;
  // }

  return res;
}

/**
* This function return all news stored
* @return res news list
**/
function getAllNews () {
  return newsList;
}

/**
* This function returns a subset of news with the specified category's name
* @param category the name to find
* @return res if the news found or not
**/
function getNewsTitlesByCategory(category){

  // console.log(category);

  var result = [];
  for (var i = 0; i < newsList.length; i++) {
    if(newsList[i].category.name === category.name) {
      result.push(newsList[i]);
    }
  }

  return result;

}


async function getNewsTitleAudioByNewsId(news){
  var result;

  for (var i = 0; i < newsList.length; i++) {
    if(newsList[i].newsId === news.newsId) {
      result = newsList[i];
    }
  }

  if (result !== undefined && result.titleAudioPath == undefined){
    result.titleAudioPath = await tts.tts(result.newsId, "title", result.title, newsLanguage);
  }


  console.log("============================"+result.titleAudioPath);

  return result;

}


/**
* This function returns a news with the specified id
* @param news the newstitle used to find the news
* @return res if the news found or not
**/
function getNewsById(news){

  var newNews;

  for (var i = 0; i < newsList.length; i++) {

    if(newsList[i].newsId === news.newsId) {
      // console.log(i);
      newNews = newsList[i];
    }
  }

  return newNews;

}

async function getNewsDescriptionAudioByNewsId(news){

  var newNews = getNewsById(news);
  console.log("============================"+newNews);

  // if the item is found
  if (newNews !== undefined && newNews.descritpionAudioPath == undefined){
    try {
      newNews.descritpionAudioPath = await tts.tts(newNews.newsId, "description", newNews.description, newsLanguage);
    } catch (e) {
      console.log(e);
    } finally {
      console.log("----------------DESCR AUDIOPATH: "+newNews.descritpionAudioPath);
    }
  }

  return newNews;

}

function cleanNews () {
  newsList = [];
}

var newsTest = new News();
newsTest.newsId= "_fh7hvrb1f";
newsTest.title = "Social utenti lamentosi";
newsTest.category = new Category("general");
newsTest.description = "Sui social moltissimi utenti dei gestori più famosi lamentano una situazione assolutamente paradossale. Infatti, secondo molti clienti, i \"soliti noti\", invece di scalare i minuti dalle promozioni, applicano costi qualora si facessero telefonate verso un nume…Sui social moltissimi utenti dei gestori più famosi lamentano una situazione assolutamente paradossale. Infatti, secondo molti clienti, i \"soliti noti\", invece di scalare i minuti dalle promozioni, applicano costi qualora si facessero telefonate verso un nume…"
// newsTest.descritpionAudioPath = ['/Users/giovanni/Dropbox/Uni/EIT/ICT Inn/Joni/Server/recordings/_fh7hvrb1f/0.mp3','/Users/giovanni/Dropbox/Uni/EIT/ICT Inn/Joni/Server/recordings/_fh7hvrb1f/1.mp3'];
newsList.push(newsTest);

// Scheduling dell'update
var j = schedule.scheduleJob('0 */15 * * * *', function(){
  updateNews();
  console.log('News Updated');
});


exports.isValid = isValid;
exports.updateNews = updateNews;
exports.addNews = addNews;
exports.getAllNews = getAllNews;
exports.getNewsTitlesByCategory = getNewsTitlesByCategory;
exports.getNewsById = getNewsById;
exports.getNewsDescriptionAudioByNewsId = getNewsDescriptionAudioByNewsId;
exports.getNewsTitleAudioByNewsId = getNewsTitleAudioByNewsId;
exports.cleanNews = cleanNews;
