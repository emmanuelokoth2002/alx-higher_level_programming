#!/bin/bash
# Script that displays all HTTP methods accepted by a server for a URL
curl -sI "$1" | grep "Allow:" | cut -d ' ' -f2-
