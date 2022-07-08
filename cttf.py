#!/usr/bin/env python

import ffmpeg, os
from mutagen.flac import FLAC


FROM_CODEC = "flac"
TO_CODEC = "mp3"
FORMAT_STRING = "{TITLE} - {ARTIST}.{TO_CODEC}"

#Recursively add files matching FROM_CODEC to the list
original_files = []
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(FROM_CODEC):
            path = os.path.join(root, file)
            original_files.append(path)

print(f"Found {len(original_files)} files")

#Process files in the list
for file in original_files:
    audio = FLAC(file)
    album_folder = os.path.dirname(file)

    #Create converted folder
    if not os.path.exists(f"{album_folder}/processed"):
       os.makedirs(f"{album_folder}/processed")
    
    #Extract cover image if it doesn't exist
    if not os.path.exists(f"{album_folder}/cover.jpg") and audio.pictures[0]:
        open(f"{os.path.dirname(file)}/cover.jpg", 'wb').write(audio.pictures[0].data)
    if audio.tags is None:
        print(f"[ERR] NO TAGS ON {file}")

    #Assemble new filename
    new_name = f"{os.path.dirname(file)}/{FORMAT_STRING.format(TITLE=audio['title'][0], ARTIST=audio['albumartist'][0],TO_CODEC=TO_CODEC)}"

    #Transcode
    stream = ffmpeg.input(file)
    stream = ffmpeg.output(stream, new_name, audio_bitrate='320k')
    ffmpeg.run(stream)
    
    #Move original file to processed
    os.rename(file, f"{album_folder}/processed/{os.path.basename(file)}" )
    