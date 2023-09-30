url = input('Enter URL - ')

import yt_dlp as youtube_dl
from yt_dlp.postprocessor import FFmpegPostProcessor
FFmpegPostProcessor._ffmpeg_location.set(R'C:\Users\chauhan\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\youtube_dl\ffmpeg-6.0')

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


	
