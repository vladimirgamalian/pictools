#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils import get_file_list


def merge_file(file_name, sample, back):
    im = Image.open(file_name)
    sm = Image.open(sample)
    assert im.size == sm.size
    if back:
        sm.paste(im, None, im)
        sm.save(file_name)
    else:
        im.paste(sm, None, sm)
        im.save(file_name)


@click.command()
@click.argument('sample', type=click.Path(exists=True, dir_okay=False))
@click.argument('path', type=click.Path(exists=True))
@click.option('--back', is_flag=True, help='sample under picture')
def merge(sample, path, back):
    for f in get_file_list(path):
        merge_file(f, sample, back)


if __name__ == '__main__':
    merge()
