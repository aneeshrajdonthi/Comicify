import cv2,os
import img2pdf,textwrap
from natsort import natsorted
def midtimediff(start_time, end_time):
    start_minutes, start_seconds = map(int, start_time.split(":"))
    end_minutes, end_seconds = map(int, end_time.split(":"))

    start_total_seconds = start_minutes * 60 + start_seconds
    end_total_seconds = end_minutes * 60 + end_seconds

    total_seconds = (start_total_seconds + end_total_seconds) / 2
    timestamp_minutes, timestamp_seconds = divmod(total_seconds, 60)
    timestamp = "{:02d}:{:02d}".format(int(timestamp_minutes), int(timestamp_seconds))
    return timestamp

def timediffsec(start_time, end_time):
    start_minutes, start_seconds = map(int, start_time.split(":"))
    end_minutes, end_seconds = map(int, end_time.split(":"))

    # Convert minutes and seconds to seconds for easier calculation
    start_total_seconds = start_minutes * 60 + start_seconds
    end_total_seconds = end_minutes * 60 + end_seconds

    # Calculate the time difference in seconds
    time_difference = abs(start_total_seconds - end_total_seconds)

    return time_difference

def frametommss(video):
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = video.get(cv2.CAP_PROP_FPS)
    total_seconds = frame_count / frame_rate
    # Convert to minutes and seconds
    minutes, seconds = divmod(total_seconds, 60)
    # Format the time as "mm:ss"
    time_formatted = "{:02d}:{:02d}".format(int(minutes), int(seconds))
    return time_formatted



def converttopdf(dirname):
    imgs = []
    for fname in os.listdir(dirname):
        if not fname.endswith(".jpg"):
            continue
        path = os.path.join(dirname, fname)
        if os.path.isdir(path):
            continue
        imgs.append(path)
    imgs = natsorted(imgs)
    with open("output.pdf","wb") as f:
        f.write(img2pdf.convert(imgs))

def deletefiles(dirname):
    for filename in os.listdir(dirname):
        os.remove(os.path.join(dirname,filename))

def textonImage(image,text,font,font_size,thickness):
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_size, thickness)
    (char_width, char_height), _ = cv2.getTextSize('W', font, font_size, thickness)
    wrapped_text = textwrap.wrap(text, width=(image.shape[1]/char_width))
    for i, line in enumerate(wrapped_text):
        textsize = cv2.getTextSize(line, font, font_size, thickness)[0]

        gap = textsize[1] + 10
        y = image.shape[0]-(len(wrapped_text)-i)*gap
        x = 20

        cv2.putText(image, line, (x, y), font,font_size, (0,0,0), thickness+1, lineType = cv2.LINE_AA)
        cv2.putText(image, line, (x, y), font,font_size, (255,255,255), thickness, lineType = cv2.LINE_AA)
    