#!/usr/bin/node

const { dict } = require('./101-data');

console.log(dict);

const newDict = {};
for (const [userId, occurrences] of Object.entries(dict)) {
  if (occurrences in newDict) {
    newDict[occurrences].push(userId);
  } else {
    newDict[occurrences] = [userId];
  }
}

console.log(newDict);
