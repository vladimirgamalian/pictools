#!/usr/bin/python

import time


class StupidTimer:
    def __init__(self, t):
        self.t = time.clock() + t

    def finished(self):
        return time.clock() > self.t
