#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let count = 0; count < x * 2; count++) {
    theFunction();
  }
};
