#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils.misc import get_file_list


@click.command()
@click.argument('path', type=click.Path(exists=True))
def set_corners(path):
    """
    Set pixels (1, 1, 1, 1) at image corners
    """
    for f in get_file_list(path):
        img = Image.open(f)
        if img.mode == 'RGBA':
            right = img.size[0] - 1
            bottom = img.size[1] - 1
            pixels = img.load()
            pixel = (1, 1, 1, 1)
            pixels[0, 0] = pixel
            pixels[right, 0] = pixel
            pixels[right, bottom] = pixel
            pixels[0, bottom] = pixel
            img.save(f)


if __name__ == '__main__':
    set_corners()
