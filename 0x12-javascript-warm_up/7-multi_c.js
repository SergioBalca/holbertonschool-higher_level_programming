#!/usr/bin/node

const args = process.argv;
const message = 'C is fun';
const argInt = parseInt(args[2]);
let count = 0;

if (argInt) {
  while (count < argInt) {
    console.log(message);
    count++;
  }
} else {
  console.log('Missing number of ocurrences');
}
