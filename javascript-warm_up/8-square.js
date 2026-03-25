#!/usr/bin/node

const args = process.argv.slice(2);

// first argument is the size of the square
const squareSize = parseInt(args[0]);

if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    console.log('X'.repeat(squareSize));
  }
}
