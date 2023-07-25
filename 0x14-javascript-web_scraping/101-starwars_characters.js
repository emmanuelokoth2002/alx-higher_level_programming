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

      // Use a counter to keep track of the characters
      let count = 0;

      // Function to fetch and print the character's name based on the character URL
      const fetchCharacter = (characterUrl) => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            if (charResponse.statusCode === 200) {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
              count++;

              // If all characters are fetched, exit the script
              if (count === charactersUrls.length) {
                process.exit();
              }
            } else {
              console.error(`Error: ${charResponse.statusCode}`);
            }
          }
        });
      };

      // Fetch and print the characters in the same order as the list "characters" in the /films/ response
      charactersUrls.forEach(fetchCharacter);
    } else {
      console.error(`Error: ${response.statusCode}`);
    }
  }
});
