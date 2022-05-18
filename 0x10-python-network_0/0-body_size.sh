#!/bin/bash
# Takes in a URL, sends a request to that URL, and
# displays the size of the body of the response
# to get a single header, the grep command is used

curl -s -I "$1" | grep Content-Length | cut -d ":" -f 2 | cut -d " " -f 2
