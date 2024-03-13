#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  let nb = 1;
  while (number > 0) {
    nb++;
	number--;
  }
  theFunction(nb);
};
