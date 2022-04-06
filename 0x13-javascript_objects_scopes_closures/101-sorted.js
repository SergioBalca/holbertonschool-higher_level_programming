#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const key of Object.keys(dict)) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
