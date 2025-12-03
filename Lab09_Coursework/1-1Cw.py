#!/usr/bin/env python3

import random,os

EMPTY='.'
CASUALTY='C'
SEARCHED='~'

class Environment():
    def __init__(self,width=20,height=10):
        self.width=width
        self.height=height
        self.grid=[[EMPTY for _ in range(width)]for _ in range(height)]
    def display(self):
        for row in self.grid:
            print(''.join(row))
    def clear_screen(self):
        os.system('cls'if os.name=='nt'else'clear')
    def place_casualty(self,x=None,y=None):
        if x is None:x=random.randint(0,self.width-1)
        if y is None:y=random.randint(self.height-2,self.height-1)
        self.grid[y][x]=CASUALTY
        return(x,y)

def Agent():
    def __init__(self,name,x,y):
        self.name=name
        self.x=x
        self.y=y
        self.search_range=1
    def move_towards(self,target_x,target_y):
        if self.x<target_x:self.x+=1
        elif self.x>target_x:self.x-=1
        elif self.y<target_y:self.y+=1
        elif self.y>target_y:self.y-=1

def main():
    env=Environment(20,10)
    pos=env.place_casualty()
    print(f"casualty hidden at {pos}")
    env.display()

if __name__=="__main__":
    main()