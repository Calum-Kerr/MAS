#!/usr/bin/env python3

import random,os,asyncio

EMPTY='.'
CASUALTY='C'
SEARCHED='~'

class Environment():
    def __init__(self,width=21,height=10):
        self.width=width
        self.height=height
        self.grid=[[EMPTY for _ in range(width)]for _ in range(height)]
    def display(self,agents=None,highlights=[]):
        for y in range(self.height):
            row=''
            for x in range(self.width):
                if agents and any(a.x==x and a.y==y for a in agents):row+='P'
                elif(x,y) in highlights:row+='*'
                else:row+=self.grid[y][x]
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
    def get_view_cone(self,env,length=5):
        cells=[]
        for d in range(1,length+1):
            for w in range(-d,d+1):
                nx,ny=self.x+w,self.y+d
                if 0<=nx<env.width and 0<=ny<env.height:cells.append((nx,ny))
        return cells

async def main():
    env=Environment(21,10)
    pos=env.place_casualty()
    print(f"casualty hidden at {pos}")
    agent=Agent("agent0",11,0)
    while not agent.search(env):
        env.clear_screen()
        cone=agent.get_view_cone(env)
        env.display([agent],cone)
        agent.y+=1
        await asyncio.sleep(0.2)

if __name__=="__main__":
    asyncio.run(main())