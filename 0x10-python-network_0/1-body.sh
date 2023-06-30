#!/bin/bash
# Script that sends a GET request to a URL and displays the body of the response if status code is 200
# Check if the URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send the GET request using curl with silent mode and store the response body in a variable
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Check if the status code is 200
if [ "$response" -eq 200 ]; then
  # Display the body of the response using curl with silent mode
  curl -s "$1"
fi
