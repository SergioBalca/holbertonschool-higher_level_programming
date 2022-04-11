#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');

request(args[0], (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
