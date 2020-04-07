#!/bin/sh

# Tool to do batches of crops.
# takes a list of video files

while read p; do
    filename=`echo "$p" | cut -d ',' -f 1`
    start=`echo "$p" | cut -d ',' -f 2`
    end=`echo "$p" | cut -d ',' -f 3`

    cat /dev/null | `dirname "$0"`/crop.sh "$filename" "$start" "$end"

done <$1

