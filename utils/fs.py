#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import contextlib
from utils.stupid_timer import StupidTimer


def is_iterable(o):
    try:
        _ = iter(o)
    except TypeError:
        return False
    return True


def remove_tree(d, ignore_non_exists=True):
    if not os.path.exists(d):
        if ignore_non_exists:
            return
        else:
            raise Exception('dir ' + d + ' not exists')

    if not os.path.isdir(d):
        raise Exception(d + ' is not a dir')

    t = StupidTimer(1)
    while os.path.exists(d):
        if t.finished():
            raise Exception('can not remove dir ' + d)
        with contextlib.suppress(Exception):
            shutil.rmtree(d)


def remove_file(f, ignore_non_exists=True):
    if is_iterable(f) and not isinstance(f, basestring):
        for i in f:
            remove_file(i, ignore_non_exists)
        return

    if not os.path.exists(f):
        if ignore_non_exists:
            return
        else:
            raise Exception('file ' + f + ' not exists')

    if not os.path.isfile(f):
        raise Exception(f + ' is not a file')

    t = StupidTimer(1)
    while os.path.exists(f):
        if t.finished():
            raise Exception('can not remove file ' + f)
        try:
            os.remove(f)
        except OSError:
            pass


def recreate_dir(d):
    if not isinstance(d, str):
        for i in d:
            recreate_dir(i)
        return

    remove_tree(d)
    t = StupidTimer(1)
    while True:
        with contextlib.suppress(Exception):
            os.makedirs(d)
        if os.path.isdir(d):
            break
        if t.finished():
            raise Exception('can not recreate dir ' + d)


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
