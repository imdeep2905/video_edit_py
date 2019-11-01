import cv2
from PIL import Image
import os
import play_video.py
########
def diff(image1, image2):
    i1 = Image.open(image1)
    i2 = Image.open(image2)
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
    ncomponents = i1.size[0] * i1.size[1] * 3
    print(f'DIFF {image1} and {image2} ==> {(dif / 255.0 * 100) / ncomponents}')
    return (dif / 255.0 * 100) / ncomponents


def make_video_frames():
    vid_frames = []
    prev_diff = 1
    for i in range(1, cnt):
        if (diff(f'frame{prev_diff}.jpg', f'frame{i}.jpg')) >= 10:
            prev_diff = i
            print('found frame!!')
            vid_frames.append(i)
       # elif (diff(f'frame{i}.jpg', f'frame{i + 1}.jpg') < 2):
        #    print('found frame!!')
         #   vid_frames.append(i)
    print(vid_frames)
    image_folder = '.'
    video_name = 'edited.avi'
    frame = cv2.imread(os.path.join(image_folder, f'frame{0}.jpg'))
    height, width = 480, 848
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    for i in vid_frames:
        video.write(cv2.imread(os.path.join(image_folder, f'frame{i}.jpg')))
    cv2.destroyAllWindows()
    video.release()



try:
    cnt = 0
    cap = cv2.VideoCapture('test.mp4')
    if (cap.isOpened() == False):
        print("Error opening video stream or file")
    while (cap.isOpened()):
        ret, frame = cap.read()
        cv2.imwrite("frame.jpg", frame)
        if True:
            cnt+=1
            Image.open('frame.jpg').save(f'frame{cnt}.jpg')
            if ret == True:
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
        if cnt == 3594:
            break
    cap.release()
    cv2.destroyAllWindows()
    make_video_frames()
except OSError:
    pass
except IOError:
    pass
