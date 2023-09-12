#!/usr/bin/node
const arg = parseInt(process.argv[2]);

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  let count = arg;
  while (count > 0) {
    console.log('X'.repeat(arg));
    count--;
  }
}
