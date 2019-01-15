#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
from PIL import Image
from utils.misc import make_dir_by_file_name


def parse_line(line, src_size):
    tokens = line.split()
    if len(tokens) != 5:
        raise Exception()
    x = int(tokens[1])
    y = int(tokens[2])
    w = int(tokens[3])
    h = int(tokens[4])
    if x < 0 or y < 0 or w < 1 or h < 1 or x + w > src_size[0] or y + h > src_size[1]:
        raise Exception()
    return {'dst_file': tokens[0], 'rect': (x, y, x + w, y + h)}


def parse_info_file(info_file, src_size):
    result = []
    with open(info_file) as f:
        for i, line in enumerate(f):
            try:
                result.append(parse_line(line, src_size))
            except Exception:
                raise RuntimeError('error parse line #' + str(i + 1) + ': ' + line)
    return result


@click.command()
@click.argument('info_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('path', type=click.Path(exists=True, dir_okay=False))
def multi_cut(info_file, path):
    """
    extract many regions from given picture by text file data
    """
    out_dir = make_dir_by_file_name(path)
    img = Image.open(path)
    cut_info = parse_info_file(info_file, img.size)
    for cut in cut_info:
        dst_file = os.path.join(out_dir, cut['dst_file'])
        img.crop(cut['rect']).save(dst_file)


if __name__ == '__main__':
    multi_cut()
