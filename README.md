# Usage
```
python generate_srt.py <lang> <input-file>
```
or
```
python generate_srt_multi.py <lang> <directory>
```
(Specify preferred whisper model in generate_srt.py)

# What it does
generate_srt.py generates subtitles for a given video in a given language using faster_whisper.
generate_srt_multi.py does the same thing, but for every video found in the given directory.
