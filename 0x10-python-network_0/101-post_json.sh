#!/bin/bash
# Json
curl -sX POST $1 -H "Content-Type: application/json" -d @$2
