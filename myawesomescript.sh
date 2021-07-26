#!/bin/bash
curl -s $1 | grep "https" | cut -d '"' -f 2
exit 0
