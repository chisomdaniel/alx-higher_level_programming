#!/usr/bin/node

exports.esrever = function (list) {
    let newList = [];
    for (let i = 1; i < list.length + 1; i++) {
        newList.push(list[list.length-i]);
    }
    return newList;
}
