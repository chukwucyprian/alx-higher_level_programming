#!/bin/bash
# Send a GET request to a given URL with a header variable.
curl -sH "X-school-User-Id: 98" "${1}"
