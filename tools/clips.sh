#!/bin/sh

t=`basename "$1"`
output="clips/${t%%.*}-$2.mp4"

ffmpeg -i "$1" -ss $2 -t 5 -c:v h264_nvenc -acodec copy -async 1 "$output" 
