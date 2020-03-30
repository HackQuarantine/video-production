#!/bin/sh
input=$1
output=$2

opening=`pwd`/assets/opening.mkv
staging=`pwd`/staging/`dd if=/dev/urandom bs=1 count=16 2>/dev/null | xxd -ps`.mkv
closing=`pwd`/assets/stinger.mkv

start=$3
end=$4

# What we need to crop from the side
x_start=240
y_start=135

# Can't use libfdk_aac as I do not have the non-free extensions installed.
ffmpeg -i $input -vf "crop=w=in_w-$x_start:h=in_h-$y_start:x=$x_start:y=0,scale=1920x1080,setsar=1:1,fade=in:0:24" -c:v libx264 -c:a aac -async 1 -ss $start -to $end $staging

ffmpeg -i $opening -i $staging -i $closing -filter_complex "[0:v:0][0:a:0][1:v:0][1:a:0][2:v:0][2:a:0]concat=n=3:v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" $output
