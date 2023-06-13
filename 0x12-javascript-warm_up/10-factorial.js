#!/usr/bin/node
function factorial (y) {
  if (isNaN(y) || y < 2) { return 1; } else { return (y * factorial(y - 1)); }
}

console.log(factorial(process.argv[2]));
