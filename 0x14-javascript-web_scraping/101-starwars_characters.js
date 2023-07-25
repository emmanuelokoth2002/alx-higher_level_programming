#!/usr/bin/node

const request = require('request');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API endpoint for the given movie ID
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const charactersUrls = movieData.characters;

      // Use a counter and a recursive function to fetch and print characters sequentially
      let count = 0;

      const fetchAndPrintCharacter = () => {
        if (count === charactersUrls.length) {
          // All characters have been fetched, exit the script
          process.exit();
        }

        const characterUrl = charactersUrls[count];
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            if (charResponse.statusCode === 200) {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
              count++;
              fetchAndPrintCharacter(); // Fetch the next character
            } else {
              console.error(`Error: ${charResponse.statusCode}`);
            }
          }
        });
      };

      fetchAndPrintCharacter(); // Start fetching and printing characters
    } else {
      console.error(`Error: ${response.statusCode}`);
    }
  }
});
