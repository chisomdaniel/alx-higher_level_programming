#!/usr/bin/node

let num = parseInt(process.argv[2]);
const num2 = num;

if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (num && num >= 0) {
    console.log('X'.repeat(num2));
    num = num - 1;
  }
}
