#!/usr/bin/node

export.addMeMaybe = function addMeMaybe(number, theFunction) {
  number++;
  theFunction(number);
}
