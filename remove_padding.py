#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils import get_file_list


def box_union(a, b):
    left = min(a[0], b[0])
    top = min(a[1], b[1])
    right = max(a[2], b[2])
    bottom = max(a[3], b[3])
    return left, top, right, bottom


@click.command()
@click.argument('path', type=click.Path(exists=True))
def crop(path):
    files = get_file_list(path)
    sizes = [Image.open(f).size for f in files]
    assert all(s == sizes[0] for s in sizes)
    boxes = [Image.open(f).convert("RGBa").getbbox() for f in files]
    box = reduce(box_union, boxes)
    for f in files:
        img = Image.open(f)
        img.crop(box).save(f)


if __name__ == '__main__':
    crop()
