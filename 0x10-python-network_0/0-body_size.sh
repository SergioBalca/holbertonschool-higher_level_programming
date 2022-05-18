#!/bin/bash
# Takes in a URL, sends a request to that URL, ana displays the size
curl -s -I "$1" | grep Content-Length | cut -d ":" -f 2 | cut -d " " -f 2
