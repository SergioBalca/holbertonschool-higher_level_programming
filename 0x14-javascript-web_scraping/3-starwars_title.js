#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const string = 'https://swapi-api.hbtn.io/api/films/' + args[0];

request(string, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(response.body);
    console.log(obj.title);
  }
});
