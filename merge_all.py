#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils import get_file_list


def merge_images(im, file_name, no_alpha):
    print file_name
    sm = Image.open(file_name)
    assert im.size == sm.size
    if no_alpha:
        im.paste(sm, None, sm)
    else:
        mask = Image.new('L', im.size, color=127)
        im.paste(sm, None, mask)
    return im


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.argument('output', type=click.Path(dir_okay=False))
@click.option('-v', '--no_alpha', is_flag=True, help='flip vertical')
def merge_all(path, output, no_alpha):
    """
    """
    file_list = get_file_list(path)
    assert len(file_list) > 1
    im = Image.open(file_list[0])
    for f in file_list:
        im = merge_images(im, f, no_alpha)
    im.save(output)


if __name__ == '__main__':
    merge_all()
