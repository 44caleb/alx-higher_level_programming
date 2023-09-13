#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  function print() {
    for (let ht = 0; ht < this.height; ht++) {
      console.log('X'.repeat(this.width));
    }
  }
};
