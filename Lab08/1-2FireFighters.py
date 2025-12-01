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
    def display(self):
        for row in self.grid:
            print(''.join(row))
        print()
    def start_fire(self,x,y):
        if 0<=x<self.width and 0<=y<self.height:
            self.grid[y][x]=FIRE

def main():
    env=Environment(10,10)
    env.start_fire(5,5)
    env.display()

if __name__=="__main__":
    main()