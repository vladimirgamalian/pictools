#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils import get_file_list


@click.command()
@click.argument('path', type=click.Path(exists=True))
def is_eq_size(path):
    """
    Test all pictures in folder (recursive) for size equality.
    """
    files = get_file_list(path)
    sizes = [Image.open(f).size for f in files]

    if all(s == sizes[0] for s in sizes):
        print 'all pictures have same size'
    else:
        print 'not all pictures have same size'


if __name__ == '__main__':
    is_eq_size()
