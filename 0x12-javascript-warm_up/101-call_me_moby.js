#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let num = x;
  while (num) {
    theFunction();
    num = num - 1;
  }
};
