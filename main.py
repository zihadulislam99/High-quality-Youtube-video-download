# pip install yt-dlp

import yt_dlp

ydl_opts = {
    "verbose": True,
    "format": "bestvideo+bestaudio",
    "merge_output_format": "mp4",
    "ffmpeg_location": r"F:\Work Shop\..PYTHON\TZ_Mini_GPT\ffmpeg-master-latest-win64-gpl-shared\bin",
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([
        "https://www.youtube.com/watch?v=8iOg9aAY0NQ"
    ])
