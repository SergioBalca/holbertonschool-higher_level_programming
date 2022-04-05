#!/usr/bin/node

const args = process.argv;
let string = '';
const argInt = parseInt(args[2]);

if (argInt) {
  for (let column = 0; column < argInt; column++) {
    for (let row = 0; row < argInt; row++) {
      string += 'X';
    }
    if (column !== argInt - 1) {
      string += '\n';
    }
  }
  console.log(string);
} else {
  console.log('Missing size');
}
