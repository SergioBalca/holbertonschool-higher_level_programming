#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

const file = fs.readFileSync(args[0], { encoding: 'utf-8' });
console.log(file);
