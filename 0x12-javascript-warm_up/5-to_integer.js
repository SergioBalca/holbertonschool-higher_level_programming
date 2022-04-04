#!/usr/bin/node

const args = process.argv;

const argInt = parseInt(args[2]);
if (argInt) {
  console.log('My number: ' + argInt);
} else {
  console.log('Not a number');
}
