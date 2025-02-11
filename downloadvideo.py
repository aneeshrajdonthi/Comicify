from pytube import YouTube
import os

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename='videoclip.mp4')
    except:
        print("An error has occurred")
    print("Download is completed successfully")
def DownloadAudio(link):
    youtubeObject = YouTube(link)
    audio = youtubeObject.streams.filter(only_audio=True).first()
    out_file = audio.download(output_path='')
    base, ext = os.path.splitext(out_file)
    new_file = 'videoaudio.mp3'
    os.rename(out_file, new_file)
