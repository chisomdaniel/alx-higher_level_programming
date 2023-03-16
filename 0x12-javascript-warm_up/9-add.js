#!/usr/bin/node

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);
let sum;

function add (a, b) {
  return a + b;
}

if (isNaN(first) || isNaN(second)) {
  console.log('NaN');
} else {
  sum = add(first, second);
  console.log(sum);
}
