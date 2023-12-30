from time import time

import PIL.Image
import torch
from matplotlib import pyplot as plt
from ultralytics import YOLO
from ultralytics import RTDETR
from plotting.plotting import draw_image



torch.backends.cudnn.benchmark = True

#maybe try tensorRT?

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#model = YOLO('yolov8n-seg.pt').cuda()  #this is downscaling the image??
model = RTDETR('rtdetr-l.pt').cuda()

test_img = 'BeforeObjectDetection.png'

# Predict with the model
for i in range(1):
    a = time()
    results = model(test_img)
    b = time()
    print(f'{i} time taken: {b - a}')
print(f'------------------------------')
print(type(results))
print(len(results))
#print(results[0].boxes)

colors = []
for i in range(15):
    temp = torch.randint(low=0, high=255, size=[3])
    colors.append(temp)

colors = ['#1f77b4',
    '#ff7f0e',
    '#2ca02c',
    '#d62728',
    '#9467bd',
    '#8c564b',
    '#e377c2',
    '#7f7f7f',
    '#bcbd22',
    '#17becf',
    '#ff7f0e',
    '#2ca02c',
    '#d62728',
    '#9467bd',
    '#8c564b',
    '#e377c2',
    '#7f7f7f',
    '#bcbd22',
    '#17becf',
    '#ff7f0e',
    '#2ca02c',
    '#d62728',
    '#9467bd',
    '#8c564b',
    '#e377c2',
    '#7f7f7f',
    '#bcbd22',
    '#17becf',
    '#d62728',
    '#9467bd',
    '#8c564b',
    '#e377c2',
    '#7f7f7f',
    '#bcbd22',
    '#17becf'
          ]

print(f'boxes: {dir(results[0].boxes)}')

img = draw_image(PIL.Image.open(test_img), results[0].boxes.xyxy, results[0].boxes.cls, colors)
plt.imshow(img)
plt.show()

'''
# Load a COCO-pretrained RT-DETR-l model
# model = RTDETR('rtdetr-l.pt').cuda()
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model = torch.hub.load("ultralytics/yolov5", "yolov5s")
model = model.cuda()

# Display model information (optional)
model.info()

test_img = ['BeforeObjectDetection.png']
a = time()
results = model(test_img)
b = time()
print(f'time taken: {b - a}')
print(results)

'''
