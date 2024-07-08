#!/bin/bash
# Display methods
curl -X OPTIONS -si $1 | grep -i "Allow" | awk -F ": " '{print $2}'
