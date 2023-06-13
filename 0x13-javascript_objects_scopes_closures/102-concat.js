#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1 = args[0];
const file2 = args[1];
const destination = args[2];

try {
  const content1 = fs.readFileSync(file1, 'utf8');
  const content2 = fs.readFileSync(file2, 'utf8');

  const concatenatedContent = content1 + content2;

  fs.writeFileSync(destination, concatenatedContent);
  console.log('Files concatenated successfully!');
} catch (error) {
  console.error('An error occurred:', error.message);
}
