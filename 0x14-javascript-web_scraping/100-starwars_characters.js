#!/usr/bin/node

const args = process.argv.slice(2);
const movieId = args[0];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request({ url: url, json: true }, (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  const characters = body.characters;
  for (const line of characters) {
    request(line, (err, response, body) => {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
