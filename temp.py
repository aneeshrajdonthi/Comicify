import cv2
import textwrap

image = cv2.imread("image.jpg")
text = "This is a lf theght exceed the width of xceed the width o xceed the width o xceed the width o he width of xceed the width o xceed the width o xceed the width o he width of xceed the width o xceed the width o xceed the width o he width of xceed the width o xceed the width o xceed the width o xceed the width o xceed the width o"
font = cv2.FONT_HERSHEY_DUPLEX
font_scale = 1
thickness = 2

def textonImage(image,text,font,font_size,thickness):
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
    (char_width, char_height), _ = cv2.getTextSize('W', font, font_scale, thickness)
    wrapped_text = textwrap.wrap(text, width=(image.shape[1]/char_width))
    for i, line in enumerate(wrapped_text):
        textsize = cv2.getTextSize(line, font, font_scale, thickness)[0]

        gap = textsize[1] + 10
        print(i,line)
        # y = int((image.shape[0] + textsize[1]) / 2) + i * gap
        y = image.shape[0]-(len(wrapped_text)-i)*gap
        # x = int((image.shape[1] - textsize[0]))
        x = 20

        cv2.putText(image, line, (x, y), font,font_scale, (255,255,255), thickness, lineType = cv2.LINE_AA)
    cv2.imwrite('out.jpg',image)

textonImage(image,text,font,font_scale,thickness)