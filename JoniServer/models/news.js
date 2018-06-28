function News (newsId, sourceId, sourceName, author, title, description, url, urlToImage, publishedAt, category, titleAudioPath, descritpionAudioPath) {
  this.newsId = newsId;
  this.sourceId = sourceId;
  this.sourceName = sourceName;
  this.author = author;
  this.title = title;
  this.description = description;
  this.url = url;
  this.urlToImage = urlToImage;
  this.publishedAt = publishedAt;
  this.category = category;
  this.titleAudioPath = titleAudioPath;
  this.descritpionAudioPath = descritpionAudioPath;
  this.errors = [];
}

module.exports = News;
