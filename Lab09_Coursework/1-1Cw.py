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
        if env.grid[self.y][self.x]==EMPTY:env.grid[self.y][self.x]=SEARCHED
        cone=self.get_view_cone(env)
        found=False
        for x,y in cone:
            if env.grid[y][x]==CASUALTY:
                print(f"{self.name} found casualty at ({x},{y})")
                found=True
            elif env.grid[y][x]==EMPTY:env.grid[y][x]=SEARCHED
        return found
    def get_view_cone(self,env,length=1):
        cells=[]
        for dy in range(-length,length+1):
            for dx in range(-length,length+1):
                nx,ny=self.x+dx,self.y+dy
                if 0<=nx<env.width and 0<=ny<env.height:cells.append((nx,ny))
        return cells
    def move_random(self,env):
        moves=[(1,0),(0,1),(0,-1),(-1,0)]
        random.shuffle(moves)
        for dx,dy in moves:
            nx,ny=self.x+dx,self.y+dy
            if 0<=nx<env.width and 0<=ny<env.height:
                if env.grid[ny][nx]==EMPTY or env.grid[ny][nx]==CASUALTY:
                    self.x=nx
                    self.y=ny
                    return True
        random.shuffle(moves)
        for dx,dy in moves:
            nx,ny=self.x+dx,self.y+dy
            if 0<=nx<env.width and 0<=ny<env.height:
                self.x=nx
                self.y=ny
                return True
        return False

async def main():
    env=Environment(300,13)
    pos=env.place_casualty(299,7)
    agent=Agent("agent0",2,6)
    found=False
    while not found:
        env.clear_screen()
        cone=agent.get_view_cone(env)
        env.display([agent],cone)
        if not agent.move_random(env):break
        found=agent.search(env)
        await asyncio.sleep(0.05)

if __name__=="__main__":
    asyncio.run(main())