#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils import get_file_list


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.argument('w', type=click.IntRange(min=1))
@click.argument('h', type=click.IntRange(min=1))
@click.argument('x', type=click.INT)
@click.argument('y', type=click.INT)
def resize_canvas(path, w, h, x, y):
    for f in get_file_list(path):
        im = Image.open(f).convert('RGBA')
        bg = Image.new('RGBA', (w, h))
        bg.paste(im, (x, y), im)
        bg.save(f)


if __name__ == '__main__':
    resize_canvas()
