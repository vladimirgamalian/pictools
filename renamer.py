#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
from utils import TempDir


@click.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False))
@click.option('--start', type=click.IntRange(min=0), prompt=True)
def renamer(path, start):
    files = sorted([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.lower().endswith('.png')])
    files = [(f, ('%04d' % (start + i)) + os.path.splitext(f)[1]) for i, f in enumerate(files)]
    with TempDir(path) as t:
        for f in files:
            os.rename(os.path.join(path, f[0]), os.path.join(t, f[1]))
        for f in files:
            os.rename(os.path.join(t, f[1]), os.path.join(path, f[1]))


if __name__ == '__main__':
    renamer()
