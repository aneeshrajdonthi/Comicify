from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
import os

def genSubfromYoutube(link):
    try:
        link = link[32:] 
        srt = YouTubeTranscriptApi.get_transcript(link)
        formatter = SRTFormatter()
        srt_format = formatter.format_transcript(srt)

        with open('videosub.srt', 'w', encoding='utf-8') as srt_file:
            srt_file.write(srt_format)
        return 1
    except:
        return 0

genSubfromYoutube("https://www.youtube.com/watch?v=wUqyhyxamus")
