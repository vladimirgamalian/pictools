#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image


@click.command()
@click.argument('src', type=click.Path(exists=True, dir_okay=False))
@click.argument('dst', type=click.Path(dir_okay=False))
@click.argument('col', type=click.IntRange(min=1))
@click.argument('row', type=click.IntRange(min=1))
def multipy(src, dst, col, row):
    src_im = Image.open(src)
    w, h = src_im.size
    mask = src_im if src_im.mode == 'RGBA' else None
    dst_im = Image.new(src_im.mode, (w * col, h * row))
    for y in range(row):
        for x in range(col):
            dst_im.paste(src_im, (x * w, y * h), mask)
    dst_im.save(dst)


if __name__ == '__main__':
    multipy()
