#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def is_image_file(f):
    known_extensions = ('.jpg', '.jpeg', '.png')
    return os.path.isfile(f) and f.lower().endswith(known_extensions)


def get_files_list(paths, recursive):
    result = []
    for path in paths:
        if os.path.isdir(path):
            if recursive:
                for root, dir_names, file_names in os.walk(path):
                    for filename in file_names:
                        f = os.path.join(root, filename)
                        if is_image_file(f):
                            result.append(f)
            else:
                for filename in os.listdir(path):
                    f = os.path.join(path, filename)
                    if is_image_file(f):
                        result.append(f)
        elif is_image_file(path):
            result.append(path)
        else:
            raise RuntimeError('unknown image format ', path)
    return result


def get_file_list(path):
    return get_files_list((path,), True)
