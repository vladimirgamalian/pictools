#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils import get_file_list


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-h', '--horizontal', is_flag=True, help='flip horizontal')
@click.option('-v', '--vertical', is_flag=True, help='flip vertical')
def crop(path, horizontal, vertical):
    """
    Flip image(s) horizontal or vertical (or both). 
    """
    for f in get_file_list(path):
        img = Image.open(f)
        if horizontal:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        if vertical:
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img.save(f)


if __name__ == '__main__':
    crop()
