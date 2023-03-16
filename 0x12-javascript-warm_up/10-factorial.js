#!/usr/bin/node

const num = parseInt(process.argv[2]);
let fact;

function factorial (num) {
  if (num === 0) {
    return 1;
  } else if (num < 0) {
    return num;
  }
  return num * factorial(num - 1);
}

if (isNaN(num)) {
  console.log('1');
} else {
  fact = factorial(num);
  console.log(fact);
}
