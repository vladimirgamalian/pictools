#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
from utils import TempDir, natural_sort_key


@click.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False))
@click.option('--start', type=click.IntRange(min=0), prompt=True)
@click.option('-a', '--alphabet', is_flag=True, help='alphabet sort')
def renamer(path, start, alphabet):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.lower().endswith('.png')]
    files = sorted(files) if alphabet else sorted(files, key=natural_sort_key)
    files = [(f, ('%04d' % (start + i)) + os.path.splitext(f)[1]) for i, f in enumerate(files)]
    with TempDir(path) as t:
        for f in files:
            os.rename(os.path.join(path, f[0]), os.path.join(t, f[1]))
        for f in files:
            os.rename(os.path.join(t, f[1]), os.path.join(path, f[1]))


if __name__ == '__main__':
    renamer()
