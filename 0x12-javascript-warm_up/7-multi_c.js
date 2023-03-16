#!/usr/bin/node

let num = parseInt(process.argv[2]);
let count = 0;
const num2 = num;

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (num !== count && num >= 0) {
    console.log('C is fun');
    count = count + 1;
    num = num2; // for semistandard sake.
  }
}
