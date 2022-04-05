#!/usr/bin/node

const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);

function add (a, b) {
  const sum = a + b;

  console.log(sum);
}

add(a, b);
