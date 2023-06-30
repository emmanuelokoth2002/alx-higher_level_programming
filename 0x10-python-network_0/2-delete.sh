#!/bin/bash
# Script that sends a DELETE request to a URL and displays the body of the response
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi
curl -sX DELETE "$1"
