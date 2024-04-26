#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -siLk -X OPTIONS "$1" | grep -oiE "Allow: .+" | cut -d ' ' -f2-
