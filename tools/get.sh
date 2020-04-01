#!/bin/sh

# wrapper around wget to strip out the query strings in the urls i get.
wget $1 -O ./sources/`$(dirname "$0")/better-filename.py $1`
