#!/usr/bin/node

const args = process.argv.slice(2);

const n = parseInt(args[0]);

function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(factorial(n));
}
