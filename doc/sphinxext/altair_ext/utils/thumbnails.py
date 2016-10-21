from __future__ import division
from PIL import Image


def create_thumbnail(image_filename, thumb_filename, window_size=(180, 180),
                     backgroundSize=None, backgroundPosition=None):
    # TODO: take into accound background size and position
    im = Image.open(image_filename)
    box = [(im.size[0] - window_size[0]) // 2,
           (im.size[1] - window_size[1]) // 2,
           (im.size[0] + window_size[0]) // 2,
           (im.size[1] + window_size[1]) // 2]
    im.crop(box).save(thumb_filename)
