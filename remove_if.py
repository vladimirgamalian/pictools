#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from PIL import Image
from utils.misc import get_file_list
from utils.fs import remove_file


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.argument('condition')
@click.option('-t', '--test', is_flag=True, help='test only')
def remove_if(path, condition, test):
    count = 0
    for f in get_file_list(path):
        img = Image.open(f)
        w, h = img.size
        img.close()
        if eval(condition):
            count += 1
            print (f)
            if not test:
                remove_file(f, False)
    print count, 'file(s)'


if __name__ == '__main__':
    remove_if()
