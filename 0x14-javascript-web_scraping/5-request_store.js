#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Write the response body to the file in utf-8 encoding
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    } else {
      console.error(`Error: ${response.statusCode}`);
    }
  }
});
