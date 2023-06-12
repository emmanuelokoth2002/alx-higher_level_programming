#!/usr/bin/node

const size = process.argv[2];

if (!isNaN(size)) {
  const sizeInt = parseInt(size);
  
  for (let i = 0; i < sizeInt; i++) {
    let line = '';
    for (let j = 0; j < sizeInt; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
