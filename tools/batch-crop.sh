#!/bin/sh

# Tool to do batches of crops.
# takes a list of video files

x_start=240
y_start=135

while read p; do
    filename=`echo "$p" | cut -d ',' -f 1`
    start=`echo "$p" | cut -d ',' -f 2`
    end=`echo "$p" | cut -d ',' -f 3`
    t=`basename "$filename"`
    output=staging/${t%%.*}.mkv

    cat /dev/null | ffmpeg -hwaccel cuda -i "$filename" -vf "crop=w=in_w-$x_start:h=in_h-$y_start:x=$x_start:y=0,scale=1920x1080,setsar=1:1" -c:v h264_nvenc -c:a aac -async 1 -ss "$start" -to "$end" "$output"

done <$1

