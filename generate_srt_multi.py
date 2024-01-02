import sys, os
import generate_srt

ACCEPTED_EXTENSIONS = ['.mp4','.mkv']

def generate_srt_multi(lang, directory):
    for filename in os.listdir(directory):
        extension = os.path.splitext(filename)[1]
        if extension in ACCEPTED_EXTENSIONS:
            generate_srt.generate_srt(lang, directory + filename)

if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <lang> <directory>")
else:
    generate_srt_multi(sys.argv[1], sys.argv[2])
