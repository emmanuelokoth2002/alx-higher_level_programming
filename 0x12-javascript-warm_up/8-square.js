#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
  for (let x = 0; x < size; i++) {
    console.log('X'.repeat(size));
  }
} else { console.log('Missing size'); }
