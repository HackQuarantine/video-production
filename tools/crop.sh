#!/bin/sh
input=$1
output=$2

start=$3
end=$4

# What we need to crop from the side
x_start=240
y_start=135

ffmpeg -i $input -vf "crop=w=in_w-$x_start:h=in_h-$y_start:x=$x_start:y=0,scale=1920x1080,setsar=1:1" -c:v libx264 -c:a aac -async 1 -ss $start -to $end $output
