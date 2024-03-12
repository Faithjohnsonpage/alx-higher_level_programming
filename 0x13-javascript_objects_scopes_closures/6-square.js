#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        for (let y = 0; y < this.width; y++) {
          process.stdout.write(c);
        }
        console.log();
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
