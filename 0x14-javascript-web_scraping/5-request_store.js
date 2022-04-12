#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const fs = require('fs');
const url = args[0];
const file = args[1];

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, response.body, { encoding: 'utf-8' }, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
