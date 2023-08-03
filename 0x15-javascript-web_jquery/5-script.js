// 5-script.js

// Wait for the document to be ready before executing the script
$(document).ready(function() {
  // Register a click event handler for the <div> with ID "add_item"
  $('#add_item').click(function() {
    // Create a new <li> element with the content "Item"
    const newItem = $('<li></li>').text('Item');

    // Append the new <li> element to the <ul> with class "my_list"
    $('ul.my_list').append(newItem);
  });
});
