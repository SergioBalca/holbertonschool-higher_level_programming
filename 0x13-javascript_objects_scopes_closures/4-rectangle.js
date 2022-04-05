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

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
