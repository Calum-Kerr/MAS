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
    def display(self,agents=None):
        for y in range(self.height):
            row=''
            for x in range(self.width):
                agent_here=False
                if agents:
                    for a in agents:
                        if a.x==x and a.y==y:
                            row+='@'
                            agent_here=True
                            break
                if not agent_here:
                    row+=self.grid[y][x]
            print(row)
    def clear_screen(self):
        os.system('cls'if os.name=='nt'else'clear')
    def place_casualty(self,x=None,y=None):
        if x is None:x=random.randint(0,self.width-1)
        if y is None:y=random.randint(self.height-2,self.height-1)
        self.grid[y][x]=CASUALTY
        return(x,y)

class Agent():
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
    def search(self,env):
        if env.grid[self.y][self.x]==CASUALTY:
            print(f"{self.name} found casualty at ({self.x},{self.y})")
            return True
        return False

def main():
    env=Environment(20,10)
    pos=env.place_casualty()
    print(f"casualty hidden at {pos}")
    agent=Agent("agent0",0,0)
    while not agent.search(env):
        env.clear_screen()
        env.display([agent])
        agent.move_towards(pos[0],pos[1])
    env.display([agent])

if __name__=="__main__":
    main()