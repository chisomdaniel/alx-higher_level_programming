#!/usr/bin/node
const Squ = require('./5-square');

class Square extends Squ {
  charPrint (c = 'x') {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Square;
