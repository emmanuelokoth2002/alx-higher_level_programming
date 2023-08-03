// 6-script.js

// Wait for the document to be ready before executing the script
$(document).ready(function() {
  // Register a click event handler for the <div> with ID "update_header"
  $('#update_header').click(function() {
    // Select the <header> element using the jQuery selector
    const headerElement = $('header');

    // Update the text of the <header> element to "New Header!!!"
    headerElement.text('New Header!!!');
  });
});
