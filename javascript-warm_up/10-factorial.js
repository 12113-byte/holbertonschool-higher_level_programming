#!/usr/bin/node

const args = process.argv.slice(2);

const firstArgument = parseInt(args[0]);

function factorial (firstArgument) {
  if (firstArgument === 0 || firstArgument === 1) {
    return 1;
  }
  return firstArgument * factorial(firstArgument - 1);
}

console.log(factorial(firstArgument));
