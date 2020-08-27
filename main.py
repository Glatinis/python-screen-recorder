from PIL import ImageGrab
import numpy as np
import time
import glob
import cv2
import os

def record():
    print("Started recording")
    try:
        while True:
            path = fr"temp/img{str(len(os.listdir('temp')))}.png"
            ImageGrab.grab().save(path)
            #time.sleep(0.5)
    except KeyboardInterrupt:
        print("Ended recording")
        return

def makeVideo():
    img_array = []
    for filename in glob.glob('temp/*.png'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)


    out = cv2.VideoWriter('final_video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

def cleanTemp():
    for file in os.listdir("temp"):
        os.remove(f"temp/{file}")
        print(f"removed temp/{file}")


if __name__ == "__main__":
    cleanTemp()
    record()
    makeVideo()
    cleanTemp()
