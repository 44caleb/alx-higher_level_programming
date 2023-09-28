#!/bin/bash
# shows allowd request methods
curl -sI $1 | grep 'Allow' | cut -d ' ' -f2-
