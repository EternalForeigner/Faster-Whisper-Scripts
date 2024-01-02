import sys, os, math, subprocess
from faster_whisper import WhisperModel

MODEL_SIZE = "small"

def get_media_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

def get_segments(lang, inputFile):
    model = WhisperModel(MODEL_SIZE)
    segments, info = model.transcribe(inputFile, language=lang, beam_size=5, vad_filter=True)
    print(f"Probability is {info.language_probability}")
    return segments

def seconds_to_timestamp(value):
    hours = int(value // 3600)
    minutes = int((value % 3600) // 60)
    seconds = int(value % 60)
    millis = int((value % 1) * 1000)
    return f"{hours:0>2}:{minutes:0>2}:{seconds:0>2},{millis:0<3}"

def build_srt(inputFile, segments, medialength):
    allText = ""
    index = 1
    for segment in segments:
        allText += str(index)
        allText += os.linesep

        startTimestamp = seconds_to_timestamp(segment.start)
        endTimestamp = seconds_to_timestamp(segment.end)
        allText += f"{startTimestamp} --> {endTimestamp}"
        allText += os.linesep

        allText += f" {segment.text}"
        allText += os.linesep
        allText += os.linesep

        index += 1
        progress = round((segment.end / medialength) * 100)
        print(f"Progress: {progress}%")
    return allText

def generate_srt(lang, inputfile):
    medialength = get_media_length(inputfile)
    print(f"Generating srt file for {inputfile} ({medialength} seconds length)")

    segments = get_segments(lang, inputfile)
    srtText = build_srt(inputfile, segments, medialength)
    outputfile = os.path.splitext(inputfile)[0] + '.srt'

    with open(outputfile, "w") as f:
        f.write(srtText)
    print(f"Finished and wrote file: {outputfile}")

#start
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <lang> <input-file>")
    else:
        generate_srt(sys.argv[1], sys.argv[2])