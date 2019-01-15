#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils.misc import get_file_list
import re


def validate_dim(ctx, param, value):
    percents = False
    if value.endswith('%'):
        value = value[:-1]
        percents = True
    if not re.match(r'^\d{1,6}(\.\d{1,6})?$', value):
        raise click.BadParameter('invalid value')
    value = float(value)
    if value == 0:
        raise click.BadParameter('invalid value')
    return value, percents


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--w', callback=validate_dim, prompt=True)
@click.option('--h', callback=validate_dim, prompt=True)
def resize(path, w, h):
    """
    Resize all images in the given folder and all subfolders.
    Width and Height can be integer or float values in pixels or percents: 10, 12.5, 80%, 20.5%.
    Result size will be rounded to integer.
    """
    for f in get_file_list(path):
        im = Image.open(f).convert('RGBA')
        new_w = int(round(im.size[0] * w[0] / 100. if w[1] else w[0]))
        new_h = int(round(im.size[1] * h[0] / 100. if h[1] else h[0]))
        new_im = im.resize((new_w, new_h), Image.LANCZOS)
        new_im.save(f)


if __name__ == '__main__':
    resize()
