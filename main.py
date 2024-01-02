import glob
import os
from time import time
import PIL.Image
import numpy as np
import torch
from matplotlib import pyplot as plt
from ultralytics import YOLO
from ultralytics import RTDETR
from plotting.plotting import draw_image
from matplotlib import cm
import cv2
from PIL import Image
import time

torch.backends.cudnn.benchmark = True
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# model = YOLO('yolov8n-seg.pt').cuda()  #this is downscaling the image??
model = RTDETR('rtdetr-l.pt').cuda()

colors = ['#1f77b4']


# Function to extract frames
def FrameCapture(path):
    vidObj = cv2.VideoCapture(path)
    count = 0
    success = 1

    while success:
        if count > 400:# or count > 850:
            continue
        success, image = vidObj.read()

        if image is None:
            continue

        print(f'image: {image.shape} type: {type(image)} min: {np.min(image)} max: {np.max(image)}')

        image = image[:, :, [2, 1, 0]]

        im = Image.fromarray(image).convert('RGB')
        im.save("real_images/frame%d.jpg" % count)

        results = model("real_images/frame%d.jpg" % count)

        image = draw_image(PIL.Image.open("real_images/frame%d.jpg" % count), results[0].boxes.xyxy, results[0].boxes.cls, colors)

        print(type(image))
        image.save("test_images/frame%d.jpg" % count)

        # saved = cv2.imwrite("frame%d.jpg" % count, image)

        count += 1

        print(f'count: {count}')


path = 'C:/Users/raven/Videos/Left 4 Dead 2/Left 4 Dead 2 2021.01.12 - 22.43.44.08.DVR_Trim.mp4'
#FrameCapture(path)

frame_folder = 'test_images'


def make_gif(frame_folder):
    frames = []
    for i in range(1067):
        filename = "test_images/frame%d.jpg" % i
        isFile = os.path.isfile(filename)
        if not isFile:
            continue
        image = Image.open(filename)
        frames.append(image)


    #frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.jpg")]
    print(len(frames))
    frame_one = frames[0]
    frame_one.save("my_awesome.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)


def make_real_gif():
    frames = []
    for i in range(401):
        filename = "real_images/frame%d.jpg" % i
        isFile = os.path.isfile(filename)
        if not isFile:
            continue
        image = Image.open(filename)
        frames.append(image)


    #frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.jpg")]
    print(len(frames))
    frame_one = frames[0]
    frame_one.save("my_pred.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)

#make_gif(frame_folder)
make_real_gif()
