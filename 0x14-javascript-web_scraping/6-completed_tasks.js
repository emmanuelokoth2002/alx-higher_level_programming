#!/usr/bin/node

const request = require('request');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Make a GET request to the provided API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const tasksData = JSON.parse(body);
      const completedTasksByUser = {};

      // Count the number of completed tasks for each user
      tasksData.forEach(task => {
        if (task.completed) {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        }
      });

      console.log(completedTasksByUser);
    } else {
      console.error(`Error: ${response.statusCode}`);
    }
  }
});
