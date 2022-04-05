#!/usr/bin/node

const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  args.sort(function (a, b) {
    return b - a;
  });
  console.log(args[3]);
}
