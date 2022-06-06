#!/usr/bin/node

const request = require('request');
const args = process.argv;

const URL = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request.get(URL, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  const data = JSON.parse(body);
  data.characters.forEach((person) => {
    request.get(person, (error1, response1, body1) => {
      if (error1) {
        console.error('error:', error1);
      }
      const OneCharacter = JSON.parse(body1);
      console.log(OneCharacter.name);
    });
    return 0;
  });
});
