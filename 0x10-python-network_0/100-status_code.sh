#!/bin/bash
# Display Status code
curl -s -o /dev/null -w "%{http_code}" $1
