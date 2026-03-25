#!/usr/bin/node

const args = process.argv.slice(2);

const converted = parseInt(args[0]);

if (isNaN(converted)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${converted}`);
}
