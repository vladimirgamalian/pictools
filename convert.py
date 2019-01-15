#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
from PIL import Image
from utils.misc import get_file_list


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-f', '--file-format', required=True, type=click.Choice(['png', 'bmp']))
def convert(path, file_format):
    """
    Convert image(s) to PNG or BMP format.
    """
    for file_name in get_file_list(path):
        new_file_name = os.path.splitext(file_name)[0] + '.' + file_format
        if new_file_name != file_name:
            img = Image.open(file_name)
            img.save(new_file_name)
            os.remove(file_name)


if __name__ == '__main__':
    convert()
