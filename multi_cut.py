#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
from PIL import Image
from utils import make_dir_by_file_name


def parse_info_file(info_file, src_w, src_h):
    result = []
    with open(info_file) as f:
        for i, line in enumerate(f):
            tokens = line.split()
            if len(tokens) != 5:
                raise RuntimeError('error parse line #' + str(i + 1) + ': ' + line)
            e = {'dst_file': tokens[0], 'x': int(tokens[1]), 'y': int(tokens[2]), 'w': int(tokens[3]), 'h': int(tokens[4])}
            #TODO: check coordinates
            result.append(e)
    return result


@click.command()
@click.argument('path', type=click.Path(exists=True, dir_okay=False))
@click.argument('info_file', type=click.Path(exists=True, dir_okay=False))
def multi_cut(path, info_file):
    """
    extract many regions from given picture by text file data
    """
    out_dir = make_dir_by_file_name(path)
    img = Image.open(path)
    src_w = img.size[0]
    src_h = img.size[1]
    cut_info = parse_info_file(info_file, src_w, src_h)
    for cut in cut_info:
        dst_file = os.path.join(out_dir, cut['dst_file'])
        img.crop((cut['x'], cut['y'], cut['x'] + cut['w'], cut['y'] + cut['h'])).save(dst_file)


if __name__ == '__main__':
    multi_cut()
