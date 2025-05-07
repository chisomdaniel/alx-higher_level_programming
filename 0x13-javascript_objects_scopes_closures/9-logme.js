#!/usr/bin/node

let printed = 0;

exports.logMe = function (item) {
    printed++;
    console.log(`${printed}: ${item}`);
}
