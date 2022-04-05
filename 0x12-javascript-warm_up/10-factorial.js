#!/usr/bin/node

const n = parseInt(process.argv[2]);

function factorial (n) {
  // base case
  if (n > 1) {
    return n * factorial(n - 1);
  }

  return 1;
}

const fact = factorial(n);
console.log(fact);
