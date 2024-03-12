#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && typeof w === 'number' && typeof h === 'number') {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let y = 0; y < this.width; y++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}

module.exports = Rectangle;
