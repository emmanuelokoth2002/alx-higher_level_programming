#!/bin/bash
# Script that sends a GET request to a URL and displays the body of the response if status code is 200
# Check if the URL is provided as an argument
curl -Ls "$1"
