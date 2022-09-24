from __future__ import unicode_literals
import youtube_dl
import os

def download(url):
    if os.path.exists("audio/audio.mp3"):
        os.remove("audio/audio.mp3")
    ydl_opts = {
    'format': 'bestaudio/best',
    
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'audio/audio.mp3'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        result = ydl.extract_info("{}".format(url))
        title = result.get("title", None)
        return title
    

