"use strict";

//TTS
var downloadFile = require('./download.js');
var multi_tts = require('./multi-tts.js');
var mergeAudioFiles = require('./mergeAudioFiles.js');
// var googleTTS = require('google-tts-api');
var path = require('path');
var fs = require('fs');

async function tts (newsId, dirname, text, newsLanguage) {

  var newsDir = path.resolve(__dirname, '../recordings/'+newsId); // directory destination
  console.log(newsDir);
  var splittedFilesAudio = [];

  let finalFile;

  // if the directory does not already exist, create the main directory
  if (!fs.existsSync(newsDir)){
    fs.mkdirSync(newsDir);
  }

  var destDir = path.resolve(__dirname, '../recordings/'+newsId,dirname); // directory destination
  // create the directory for audio files
  if (!fs.existsSync(destDir)){
    fs.mkdirSync(destDir);

    // split the text file into 200 chars segments
    let splittedFilesText;
    try {
      splittedFilesText = await multi_tts.multiTTS(text, newsLanguage, 1)
    } catch (err) {
      console.log(err);
    } finally {
      console.log("---------MULTITTS done");
    }

    // download every file segment into the directory created
    let downloadedFileDest;
    for (var i = 0; i < splittedFilesText.length; i++) {
      downloadedFileDest = path.resolve(__dirname, '../recordings/'+newsId, dirname+i+'.mp3'); // file destination
      splittedFilesAudio.push(downloadedFileDest);
      try {
        await downloadFile.download(splittedFilesText[i].url, downloadedFileDest);
      } catch (err) {
        console.log(err);
      }finally {
        console.log("---------DOWNLOAD done of: "+downloadedFileDest);
      }

    }

    // merge every file audio into the directory created
    try {
      finalFile = await mergeAudioFiles.mergeAudioFiles(newsId+'_'+dirname,destDir,splittedFilesAudio);
    } catch (err) {
      console.log(err);
    } finally {
      console.log("---------MERGED")
    }


  }







  return finalFile;

}

exports.tts = tts;
