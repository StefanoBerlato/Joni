var audioconcat = require('audioconcat')
// require('es6-promise').polyfill();


// var dirDest = '/Users/giovanni/Dropbox/Uni/EIT/ICTInn/Joni/Server/recordings/_fh7hvrb1f/';
// var splittedFiles = [
//   '/Users/giovanni/Dropbox/Uni/EIT/ICTInn/Joni/Server/recordings/_fh7hvrb1f/0.mp3',
//   '/Users/giovanni/Dropbox/Uni/EIT/ICTInn/Joni/Server/recordings/_fh7hvrb1f/1.mp3',
//   '/Users/giovanni/Dropbox/Uni/EIT/ICTInn/Joni/Server/recordings/_fh7hvrb1f/2.mp3'];

// var newNews = new News();

function mergeAudioFiles (outputName, dirDest,splittedFiles) {


  return new Promise(resolve => {
    var fileMergedPath = dirDest+"/"+outputName+".mp3";
    audioconcat(splittedFiles)
      .concat(fileMergedPath)
      .on('start', function (command) {
        console.log('ffmpeg process started:', command)
      })
      .on('error', function (err, stdout, stderr) {
        console.error('Error:', err)
        console.error('ffmpeg stderr:', stderr)
      })
      .on('end', function (output) {
        console.error('Audio created in:', fileMergedPath);
        resolve(fileMergedPath);
      })

  });



}

// mergeAudioFiles(dirDest,splittedFiles);

exports.mergeAudioFiles = mergeAudioFiles;
