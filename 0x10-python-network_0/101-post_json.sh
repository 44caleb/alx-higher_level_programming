#!/bin/bash
# sends json data to a url and retireves body of response
curl -s --json @$2 $1
