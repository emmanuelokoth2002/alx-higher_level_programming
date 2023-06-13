#!/usr/bin/node
exports.callMeMoby = function callMeMoby (b, func) {
  while (b-- > 0) { func(); }
};
