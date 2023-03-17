#!/usr/bin/node

const leng = process.argv.length;
let nums;
let count = 2;
const newArr = [];

if (leng <= 3) {
  console.log('0');
} else {
  while (leng > count) {
    newArr.push(process.argv[count]);
    count = count + 1;
  }
  nums = newArr.sort(function (a, b) { return b - a; });
  console.log(nums[1]);
}
