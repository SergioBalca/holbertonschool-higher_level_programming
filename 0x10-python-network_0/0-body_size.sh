#!/bin/bash
# Takes in a URL, sends a request to that URL, ana displays the size
curl -sI "$1" | awk '/Content-Length/ { print $2 }'
