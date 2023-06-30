#!/bin/bash
# Script that sends a request to a URL and displays the size of the response body

# Check if the URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send the request using curl and store the response in a variable
response=$(curl -sI "$1")

# Extract the content-length header value from the response headers
content_length=$(echo "$response" | grep -i "Content-Length:" | awk '{print $2}' | tr -d '\r')

# Display the size of the response body in bytes
echo "$content_length"
