#!/usr/bin/node

const args = process.argv.slice(2);

const firstArgument = args[0];

for (let i = 0; i < firstArgument; i++) {
  console.log('C is fun');
}
