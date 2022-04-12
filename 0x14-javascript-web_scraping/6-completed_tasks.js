#!/usr/bin/node

const args = process.argv.slice(2);
const request = require('request');
const url = args[0];

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    const dict = {};
    const obj = JSON.parse(response.body);
    for (const item of obj) {
      if (item.completed === true) {
        if (dict[item.userId] === undefined) {
          dict[item.userId] = 0;
        }
        dict[item.userId] += 1;
      }
    }
    console.log(dict);
  }
});
