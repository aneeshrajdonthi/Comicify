import cv2,os
import extractframes
import srtsplit
import downloadvideo
import youtubesrt
import helpers
import generatesubtitle

def convertVideoToComic(youtube_link):
    res = youtubesrt.genSubfromYoutube(youtube_link) #generates subtitle
    if(res==0):
        print("Generating subs...")
        downloadvideo.DownloadAudio(youtube_link)
        generatesubtitle.transcribe_audio('videoaudio.mp3')

    downloadvideo.Download(youtube_link) #downloads youtube video

    subfile = 'videosub.srt'
    video_file = 'videoclip.mp4'

    startstr = '00:00'
    endstr = '00:00'

    dialogues = srtsplit.subtitleSplit(subfile)
    count = 0
    for frames in dialogues:
        startstr = frames[1][3:8]
        if(helpers.timediffsec(startstr,endstr)>2):
            # print(endstr,'->',startstr)
            count = extractframes.extract_frame(video_file,endstr,startstr,count)
        endstr = frames[1][20:25]
        # print(startstr,'->',endstr,frames[2])
        count = extractframes.extract_frame(video_file,startstr,endstr,count,len(frames[2])+1,frames[2])
    startstr = endstr
    video = cv2.VideoCapture(video_file)
    endstr = helpers.frametommss(video)
    if(helpers.timediffsec(startstr,endstr)>2):
        extractframes.extract_frame(video_file,startstr,endstr,count)
    video.release()
    helpers.converttopdf('frames') #convert all images to pdf
    helpers.deletefiles('frames')
    os.remove('videoclip.mp4')
    os.remove('videosub.srt')
    if(res==0):
        os.remove('videoaudio.mp3')

