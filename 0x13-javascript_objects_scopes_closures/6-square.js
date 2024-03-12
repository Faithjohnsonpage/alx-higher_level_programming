#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        for (let y = 0; y < this.width; y++) {
          process.stdout.write(c);
        }
        console.log();
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
