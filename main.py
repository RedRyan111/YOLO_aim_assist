import torch
import numpy as np
from PIL import Image, ImageDraw
import d3dshot
import time
import pydirectinput
from pynput.mouse import Button, Controller as MouseController
import pynput
import math
import keyboard

from ultralytics import YOLO

model = YOLO('')

torch.backends.cudnn.benchmark=True



# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model = model.cuda()
from utils.plots import color_list