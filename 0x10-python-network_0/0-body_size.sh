#!/bin/bash
# sends a request to a URL and display the size of in bytes
curl -s -w %{size_download} $1 -o good ; echo ''
