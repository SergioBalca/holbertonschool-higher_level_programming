#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const fileA = fs.readFileSync(args[2]);
const fileB = fs.readFileSync(args[3]);
const fileC = args[4];

fs.appendFileSync(fileC, fileA);
fs.appendFileSync(fileC, fileB);
