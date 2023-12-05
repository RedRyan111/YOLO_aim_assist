import numpy as np
from utils.plots import color_list
from PIL import Image, ImageDraw


def draw_image(img, pred, colors):
    img = Image.fromarray(img.astype(np.uint8)) if isinstance(img, np.ndarray) else img  # from np
    for *box, conf, cls in pred:
        ImageDraw.Draw(img).rectangle(box, width=4, outline=colors[int(cls) % 10])  # plot
    return img
