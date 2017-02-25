#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils import get_file_list


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.argument('x', type=click.INT)
@click.argument('y', type=click.INT)
@click.argument('w', type=click.INT)
@click.argument('h', type=click.INT)
def crop(path, x, y, w, h):
    for f in get_file_list(path):
        img = Image.open(f)
        img.crop((x, y, x + w, y + h)).save(f)


if __name__ == '__main__':
    crop()
