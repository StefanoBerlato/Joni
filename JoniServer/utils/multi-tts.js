"use strict";
require('es6-promise').polyfill();

const key = require('../lib/key');
const tts = require('../lib/api');


/*
 * Google TTS API has the limitation with the length of characters (200).
 * This example will show you how to cut the long characters into several small string and get multiple TTS urls.
 */

function multiTTS (newsText, lang, speed, timeout) {
  const MAX = 200;  // Max string length
  var text = newsText;
  const isSpace = (s, i) => /\s/.test(s.charAt(i));
  const lastIndexOfSpace = (s, left, right) => {
    for (let i = right; i >= left; i--) {
      if (isSpace(s, i)) return i;
    }
    return -1;  // not found
  };

  return key(timeout).then(key => {
    const result = [];
    const addResult = (text, start, end) => {
      const str = text.slice(start, end + 1);
      result.push({
        // id: newNews.newsId,
        text: str,
        url: tts(str, key, lang, speed)
      });
    };

    let start = 0;
    for (;;) {

      // check text's length
      if (text.length - start <= MAX) {
        addResult(text, start, text.length - 1);
        break;  // end of text
      }

      // check whether the word is cut in the middle.
      let end = start + MAX - 1;
      if (isSpace(text, end) || isSpace(text, end + 1)) {
        addResult(text, start, end);
        start = end + 1;
        continue;
      }

      // find last index of space
      end = lastIndexOfSpace(text, start, end);
      if (end === -1) {
        throw new Error('the amount of single word is over that 200.');
      }

      // add result
      addResult(text, start, end);
      start = end + 1;
    }

    return result;
  });
}

exports.multiTTS = multiTTS;
