#!/usr/bin/env python3

import random,asyncio,os

EMPTY='.'
FIRE='F'
BURNED='B'

class Environment():
    def __init__(self,width=10,height=10):
        self.width=width
        self.height=height
        self.grid=[[EMPTY for _ in range(width)] for _ in range(height)]
    def display(self,agents=None):
        for y in range(self.height):
            row=''
            for x in range(self.width):
                agent_here=False
                if agents:
                    for a in agents:
                        if a.x==x and a.y==y:
                            row+='A'
                            agent_here=True
                            break
                if not agent_here:
                    row+=self.grid[y][x]
            print(row)

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
                                if random.random()<0.2:
                                    new_fires.append((nx,ny))
        for x,y in new_fires:
            self.grid[y][x]=FIRE
        return len(new_fires)
    def clear_screen(self):
        os.system('cls' if os.name=='nt' else 'clear')

class Agent():
    def __init__(self,name,x,y):
        self.name=name
        self.x=x
        self.y=y
        self.busy=False
        self.inbox=[]
    def count_nearby_fires(self,env):
        count=0
        for y in range(self.y-1,self.y+2):
            for x in range(self.x-1,self.x+2):
                if 0<=x<env.width and 0<=y<env.height:
                    if env.grid[y][x]==FIRE:
                        count+=1
        return count
    def put_out_fire(self,env):
        if env.grid[self.y][self.x]==FIRE:
            env.grid[self.y][self.x]=EMPTY
            return True
        return False
    def move_to(self,x,y,env):
        if 0<=x<env.width and 0<=y<env.height:
            self.x=x
            self.y=y
    def find_fire(self,env):
        nearest_fire=None
        min_dist=float('inf')
        for y in range(env.height):
            for x in range(env.width):
                if env.grid[y][x]==FIRE:
                    dist=abs(x-self.x)+abs(y-self.y)
                    if dist<min_dist:
                        min_dist=dist
                        nearest_fire=(x,y)
        return nearest_fire
    def move_towards(self,x,y,env):
        if self.x<x:
            self.move_to(self.x+1,self.y,env)
        elif self.x>x:
            self.move_to(self.x-1,self.y,env)
        elif self.y<y:
            self.move_to(self.x,self.y+1,env)
        elif self.y>y:
            self.move_to(self.x,self.y-1,env)

async def main():
    env=Environment(10,10)
    env.start_fire(5,5)
    agents=[Agent("agent0",0,0),Agent("agent1",9,0),Agent("agent2",0,9)]
    for turn in range(20):
        env.clear_screen()
        env.display(agents)
        for agent in agents:
            fire=agent.find_fire(env)
            if fire:
                agent.move_towards(fire[0],fire[1],env)
                agent.put_out_fire(env)
        env.spread_fires()
        await asyncio.sleep(0.4)

if __name__=="__main__":
    asyncio.run(main())