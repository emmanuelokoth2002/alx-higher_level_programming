// 2-script.js

// Wait for the document to be ready before executing the script
$(document).ready(function() {
  // Register a click event handler for the <div> with ID "red_header"
  $('#red_header').click(function() {
    // Select the <header> element using the jQuery selector
    const headerElement = $('header');

    // Update the text color of the <header> element to red (#FF0000)
    headerElement.css('color', '#FF0000');
  });
});
