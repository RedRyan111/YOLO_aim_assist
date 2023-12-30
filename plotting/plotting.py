import numpy as np
from PIL import Image, ImageDraw


def draw_image(img, boxes, predictions, colors):
    img = Image.fromarray(img.astype(np.uint8)) if isinstance(img, np.ndarray) else img  # from np
    for box, pred in zip(boxes, predictions):
        #for *box, conf, cls in pred:
        #print(f'ind: {int(pred) % 10} pred: {pred}')
        #print(type(img))
        #print(f'box: {box}')
        if pred == 0:
            ImageDraw.Draw(img).rectangle(tuple(box), width=4, outline=colors[int(pred)])  # plot
    return img
