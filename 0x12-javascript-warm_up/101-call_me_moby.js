#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let num = x;
  while (num && num >= 1) {
    theFunction();
    num = num - 1;
  }
};
