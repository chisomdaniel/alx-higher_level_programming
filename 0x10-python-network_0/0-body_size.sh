#!/usr/bin/bash
# sends a request to a URL and display the size of in bytes
curl -s -w %{size_download} 0.0.0.0:5000 -o good ; echo ''
