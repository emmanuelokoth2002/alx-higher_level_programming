#!/usr/bin/node

const request = require('request');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = 18;

// Make a GET request to the Star Wars API endpoint to get all films
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const filmsData = JSON.parse(body).results;
      const filmsWithWedgeAntilles = filmsData.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
      console.log(filmsWithWedgeAntilles.length);
    } else {
      console.error(`Error: ${response.statusCode}`);
    }
  }
});
