#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  const value = number + 1;
  theFunction(value);
};
