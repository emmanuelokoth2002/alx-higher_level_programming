// 4-script.js

// Wait for the document to be ready before executing the script
$(document).ready(function() {
  // Register a click event handler for the <div> with ID "toggle_header"
  $('#toggle_header').click(function() {
    // Select the <header> element using the jQuery selector
    const headerElement = $('header');

    // Toggle the classes "red" and "green" on the <header> element
    headerElement.toggleClass('red green');
  });
});
