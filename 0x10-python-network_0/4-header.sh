#!/bin/bash
#sends custom request header and retrieves data
curl -s -H "X-School-User-Id: 98" $1
