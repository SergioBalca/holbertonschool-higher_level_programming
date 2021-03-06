#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const character = '18/';

request(args[0], (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(response.body);
    let count = 0;
    for (let index = 0; index < obj.results.length; index++) {
      for (let idx = 0; idx < obj.results[index].characters.length; idx++) {
        if (obj.results[index].characters[idx].endsWith(character)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
