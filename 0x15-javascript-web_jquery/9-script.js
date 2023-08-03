// 9-script.js

// Wait for the document to be ready before executing the script
$(document).ready(function() {
  // URL to fetch the translation
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

  // Make an AJAX request to the URL
  $.getJSON(url, function(data) {
    // Extract the "hello" translation from the received data
    const translation = data.hello;

    // Update the content of the <div> with ID "hello" to display the translation
    $('#hello').text(translation);
  });
});
