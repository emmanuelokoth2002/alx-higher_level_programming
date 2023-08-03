// 101-script.js

// Wait for the document to be ready before executing the script
$(document).ready(function() {
  // Register a click event handler for the <div> with ID "add_item"
  $('#add_item').click(function() {
    // Create a new <li> element with the content "Item"
    const newItem = $('<li>Item</li>');

    // Append the new <li> element to the <ul> with class "my_list"
    $('ul.my_list').append(newItem);
  });

  // Register a click event handler for the <div> with ID "remove_item"
  $('#remove_item').click(function() {
    // Select the last <li> element from the <ul> with class "my_list"
    const lastItem = $('ul.my_list li:last-child');

    // Remove the last <li> element from the <ul> with class "my_list"
    lastItem.remove();
  });

  // Register a click event handler for the <div> with ID "clear_list"
  $('#clear_list').click(function() {
    // Select all <li> elements from the <ul> with class "my_list"
    const allItems = $('ul.my_list li');

    // Remove all <li> elements from the <ul> with class "my_list"
    allItems.remove();
  });
});
