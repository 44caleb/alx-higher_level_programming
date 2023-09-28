#!/bin/bash
# sends a request and retrieves the status code of response
curl -so /dev/null -w "%{http_code}" "$1"
