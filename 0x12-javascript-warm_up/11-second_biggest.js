#!/usr/bin/node

let leng = process.argv.length
let nums;

if (leng <= 1) {
  console.log('0')
}
else {
  nums = process.argv.sort(function(a, b){return b - a});
  console.log(nums[])
}
