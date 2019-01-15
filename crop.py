#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils.misc import get_file_list


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.argument('x', type=click.IntRange(min=0))
@click.argument('y', type=click.IntRange(min=0))
@click.argument('w', type=click.IntRange(min=1))
@click.argument('h', type=click.IntRange(min=1))
def crop(path, x, y, w, h):
    for f in get_file_list(path):
        img = Image.open(f)
        img.crop((x, y, x + w, y + h)).save(f)


if __name__ == '__main__':
    crop()
