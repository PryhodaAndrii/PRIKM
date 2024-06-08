from audio_extract import extract_audio
import os

def teleg_get_audio(path2vid=""):
    path2aud = path2vid.replace("mp4", "mp3")
    extract_audio(input_path=path2vid, output_path=path2aud)
    return path2aud

