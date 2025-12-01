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
    def spread_fires(self):
        new_fires=[]
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x]==FIRE:
                    neighbours=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                    for nx,ny in neighbours:
                        if 0<=nx<self.width and 0<=ny<self.height:
                            if self.grid[ny][nx]==EMPTY:
                                if random.random()<0.5:
                                    new_fires.append((nx,ny))
        for x,y in new_fires:
            self.grid[y][x]=FIRE
        return len(new_fires)

class Agent():
    def __init__(self,name,x,y):
        self.name=name
        self.x=x
        self.y=y
        self.busy=False
    def put_out_fire(self,env):
        

def main():
    env=Environment(10,10)
    env.start_fire(5,5)
    for turn in range(5):
        print(f"Turn {turn}")
        env.display()
        env.spread_fires()

if __name__=="__main__":
    main()