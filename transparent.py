#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils import get_file_list


def make_transparent(file_name, transparency, reset):
    im = Image.open(file_name)
    if reset:
        im.putalpha(transparency)
    else:
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                px = im.getpixel((x, y))
                px = (px[0], px[1], px[2], int((px[3] / 255.0) * (transparency / 255.0) * 255))
                im.putpixel((x, y), px)
    im.save(file_name)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.argument('transparency', type=click.IntRange(min=0, max=255))
@click.option('--reset', is_flag=True, help='ignore source transparency (fast)')
def transparent(path, transparency, reset):
    for f in get_file_list(path):
        make_transparent(f, transparency, reset)


if __name__ == '__main__':
    transparent()
