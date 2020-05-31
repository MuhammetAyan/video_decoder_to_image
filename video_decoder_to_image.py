from math import floor

import cv2
import numpy as np
import sys

def printProgressBar (iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    # Print New Line on Complete
    if iteration == total:
        sys.stdout.flush()

# Opens the Video file
cap = cv2.VideoCapture('Play.mp4')
FPS = cap.get(cv2.CAP_PROP_FPS)

i = 0

oldframe = np.array([[[0, 0, 0] for y in range(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))] for x in range(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))])
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

printProgressBar(0, length - 1, prefix='Progress:', suffix='Complete', length=50)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == False:
        break
    printProgressBar(i, length - 1, prefix='Progress:', suffix='Complete', length=50)
    if i % floor(FPS) == 0:
        # print("old", oldframe.shape)
        # print("new", frame.shape)
        # print(frame)
        compare = frame == oldframe
        # print(compare.all())
        # print(f"{i}/{length}")
        if not compare.all():
            cv2.imwrite('data\\kang'+str(i)+'.jpg', frame)
            oldframe = frame
    i += 1
 
cap.release()
cv2.destroyAllWindows()
