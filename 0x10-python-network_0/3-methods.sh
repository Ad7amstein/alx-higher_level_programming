#!/bin/bash
# Display methods
curl -X OPTIONS -si example.com | grep -i "Allow" | awk -F ": " '{print $2}'
