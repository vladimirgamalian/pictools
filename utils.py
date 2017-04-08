#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import uuid


def is_image_file(f):
    known_extensions = ('.bmp', '.jpg', '.jpeg', '.png')
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


def make_dir_by_file_name(file_name):
    dir_name, file_name = os.path.split(file_name)
    file_name_wo_ext = os.path.splitext(file_name)[0]
    out_dir = os.path.join(dir_name, file_name_wo_ext)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    return out_dir


def get_unique_file_name(path):
    while True:
        temp_dir = os.path.join(path, str(uuid.uuid4()))
        if not os.path.exists(temp_dir):
            return temp_dir


class TempDir:
    def __init__(self, path):
        self.root_dir = path

    def __enter__(self):
        self.temp_dir = get_unique_file_name(self.root_dir)
        os.makedirs(self.temp_dir)
        return self.temp_dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.temp_dir)
