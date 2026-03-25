#!/usr/bin/node

const args = process.argv.slice(2);

// first arg is the first int
const a = parseInt(args[0]);
// second arg is second int
const b = parseInt(args[1]);

function add (a, b) {
  return a + b;
}

console.log(add(a, b));
