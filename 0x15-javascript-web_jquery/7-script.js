// 7-script.js

// Wait for the document to be ready before executing the script
$(document).ready(function() {
  // URL to fetch the character data
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  // Make an AJAX request to the URL
  $.ajax({
    url: url,
    dataType: 'json',
    success: function(data) {
      // Extract the character name from the received data
      const characterName = data.name;

      // Update the content of the <div> with ID "character" to display the character name
      $('#character').text(characterName);
    },
    error: function(xhr, status, error) {
      // Display an error message if the request fails
      $('#character').text('Failed to fetch character data.');
    }
  });
});
