#!/usr/bin/env python3

import random

EMPTY='.'
FIRE='F'
BURNED='B'

class Environment():
    def __init__(self,width=10,height=10):
        self.width=width
        self.height=height
        self.grid=[[EMPTY for _ in range(width)] for _ in range(height)]
    