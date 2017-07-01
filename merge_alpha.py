#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils import get_file_list


def merge_alpha_file(file_name, sample):
    im = Image.open(file_name)
    sm = Image.open(sample)
    assert im.size == sm.size
    bg = Image.new('RGBA', im.size)
    bg.paste(im, None, sm)
    bg.save(file_name)


@click.command()
@click.argument('sample', type=click.Path(exists=True, dir_okay=False))
@click.argument('path', type=click.Path(exists=True))
def merge_alpha(sample, path):
    """
    set alpha channel from sample to all images in path
    """
    for f in get_file_list(path):
        merge_alpha_file(f, sample)


if __name__ == '__main__':
    merge_alpha()
