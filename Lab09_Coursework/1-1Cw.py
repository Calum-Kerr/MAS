#!/usr/bin/env python3

import random,os,asyncio

EMPTY='.'
CASUALTY='C'
SEARCHED='~'

class Environment():
    def __init__(self,width=300,height=13):
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
        cone=self.get_view_cone(env)
        found=False
        for x,y in cone:
            if env.grid[y][x]==CASUALTY:
                print(f"{self.name} found casualty at ({self.x},{self.y})")
                found=True
            elif env.grid[y][x]==EMPTY:env.grid[y][x]=SEARCHED
        return found
    def get_view_cone(self,env,length=2):
        cells=[]
        for d in range(1,length+1):
            for w in range(-d,d+1):
                nx,ny=self.x+w,self.y+d
                if 0<=nx<env.width and 0<=ny<env.height:cells.append((nx,ny))
        return cells
    def find_unsearched(self,env):
        nearest=None
        min_dist=float('inf')
        for y in range(env.height):
            for x in range(env.width):
                if env.grid[y][x]==EMPTY:dist=abs(x-self.x)+abs(y-self.y)
                if dist<min_dist:
                    min_dist=dist
                    nearest=(x,y)
        return nearest

async def main():
    env=Environment(300,13)
    pos=env.place_casualty()
    print(f"casualty hidden at {pos}")
    agent=Agent("agent0",2,0)
    agent.direction=1
    found=False
    while not agent.search(env):
        env.clear_screen()
        cone=agent.get_view_cone(env)
        env.display([agent],cone)
        target=agent.find_unsearched(env)
        if target:agent.move_towards(target[0],target[1])
        else:break
        found+agent.search(env)
        await asyncio.sleep(0.05)

if __name__=="__main__":
    asyncio.run(main())