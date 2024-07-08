#!/usr/bin/env bash
# cURL body size

url="$1"
curl -sI $url | grep -i "Content-Length" | awk '{print $2}'
