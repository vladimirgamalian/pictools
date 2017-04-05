#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
from PIL import Image
from utils import make_dir_by_file_name


@click.command()
@click.argument('path', type=click.Path(exists=True, dir_okay=False))
@click.argument('w', type=click.IntRange(min=1))
@click.argument('h', type=click.IntRange(min=1))
def slice(path, w, h):
    """
    slice image by parts with given width and height
    """
    out_dir = make_dir_by_file_name(path)
    img = Image.open(path)
    src_w = img.size[0]
    src_h = img.size[1]
    if w > src_w or h > src_h:
        raise RuntimeError('dimension out of range')
    part_x = src_w / w
    part_y = src_h / h
    for y in range(part_y):
        for x in range(part_x):
            dst_file = os.path.join(out_dir, '{0:04d}_{1:04d}.png'.format(x, y))
            img.crop((x * w, y * h, x * w + w, y * h + h)).save(dst_file)


if __name__ == '__main__':
    slice()
