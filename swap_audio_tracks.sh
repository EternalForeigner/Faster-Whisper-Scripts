#!/bin/sh

for file in *; do
    if [ -f "$file" ]; then
        if [[ $file == *.mkv ]]; then
            mv "$file" "$file"."d"
            ffmpeg -i "$file"."d" -map 0:0 -map 0:2 -map 0:1 -disposition:a:0 default -disposition:a:1 none -c copy "$file"
            rm "$file"."d"
        fi
    fi
done
