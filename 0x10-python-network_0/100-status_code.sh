#!/bin/bash
# Send a request to the URL and save the response to a file
curl -s "$1" -o /dev/null -w "%{http_code}"
