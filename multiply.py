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
    src_im = Image.open(src).convert("RGBA")
    w = src_im.size[0]
    h = src_im.size[1]
    dst_im = Image.new('RGBA', (w * col, h * row))
    for y in range(row):
        for x in range(col):
            dst_im.paste(src_im, (x * w, y * h), src_im)
    dst_im.save(dst)


if __name__ == '__main__':
    multipy()
