#!/bin/sh
ffprobe -v quiet -print_format json -show_format $1 | jq '.format.duration | tonumber' |  awk '{print "scale=2;"$1"/60.0"}' | bc
