#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string = '';
    for (let column = 0; column < this.height; column++) {
      for (let row = 0; row < this.width; row++) {
        string += 'X';
      }
      if (column !== this.height - 1) {
        string += '\n';
      }
    }
    console.log(string);
  }
}

module.exports = Rectangle;
