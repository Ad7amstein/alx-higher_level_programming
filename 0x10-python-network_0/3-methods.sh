#!/bin/bash
# Display methods
curl -sI ALLOW $1 -L | grep -i "Allow" | awk -F ": " '{print $2}'
