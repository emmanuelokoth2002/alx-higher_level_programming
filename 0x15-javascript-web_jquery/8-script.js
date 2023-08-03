// 8-script.js

// Wait for the document to be ready before executing the script
$(document).ready(function() {
  // URL to fetch the movies data
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Make an AJAX request to the URL
  $.ajax({
    url: url,
    dataType: 'json',
    success: function(data) {
      // Extract the movies array from the received data
      const movies = data.results;

      // Select the <ul> element with ID "list_movies"
      const listElement = $('#list_movies');

      // Loop through each movie and append the title to the <ul>
      movies.forEach(function(movie) {
        const title = movie.title;
        listElement.append('<li>' + title + '</li>');
      });
    },
    error: function(xhr, status, error) {
      // Display an error message if the request fails
      $('#list_movies').append('<li>Failed to fetch movies data.</li>');
    }
  });
});
