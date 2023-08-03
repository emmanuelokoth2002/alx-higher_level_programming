// 102-script.js

// Wait for the document to be ready before executing the script
$(document).ready(function() {
  // Register a click event handler for the "Translate" button
  $('#btn_translate').click(function() {
    // Get the value entered in the "Language code" input field
    const languageCode = $('#language_code').val();

    // URL to fetch the translation
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    // Make an AJAX request to the URL
    $.getJSON(url, function(data) {
      // Extract the translation of "Hello" from the received data
      const translation = data.hello;

      // Update the content of the <div> with ID "hello" to display the translation
      $('#hello').text(translation);
    });
  });
});
