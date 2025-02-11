import cv2
import os
import helpers

def extract_frame(video_path, start_time, end_time,count,div=2,dialogue=['']):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    
    start_minutes, start_seconds = map(int, start_time.split(':'))
    end_minutes, end_seconds = map(int, end_time.split(':'))
    
    start_frame = int((start_minutes * 60 + start_seconds) * fps)
    end_frame = int((end_minutes * 60 + end_seconds) * fps)
    
    for i in range(1,div):
        frame_number = start_frame + ((end_frame - start_frame) *(i/div))
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        res, frame = video.read()
        if res:
            # You can save the frame as an image here
            x=int(frame.shape[1]*0.1)
            y=int(frame.shape[0]*0.85)
            # cv2.putText(frame,dialogue[i-1],(frame.shape[0]/4,frame.shape[1]/2),cv2.FONT_HERSHEY_DUPLEX,2,(255,255,255),2)
            cv2.putText(frame, str(count), (20,20), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 1)
            # cv2.putText(frame, dialogue[i-1], (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 3)
            # cv2.putText(frame, dialogue[i-1], (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2)
            helpers.textonImage(frame,dialogue[i-1],cv2.FONT_HERSHEY_DUPLEX,1,2)
            cv2.imwrite(os.path.join('frames',f'frame{count}.jpg'), frame)
            # print(frame_number,'::',count)
            count+=1
    video.release()
    return count

# 2 -> 1/2
# 3 -> 1/3 2/3
# 4 -> 1/4 2/4 3/4