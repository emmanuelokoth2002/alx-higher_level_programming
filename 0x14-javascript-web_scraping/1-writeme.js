#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file_path> <content_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write the string content to the file in utf-8
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
