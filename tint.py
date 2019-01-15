#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image, ImageChops
from utils.misc import get_file_list, validate_color


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.argument('color', callback=validate_color)
def tint(path, color):
    for f in get_file_list(path):
        img = Image.open(f)
        img = ImageChops.multiply(img, Image.new('RGBA', img.size, color))
        img.save(f)


if __name__ == '__main__':
    tint()
