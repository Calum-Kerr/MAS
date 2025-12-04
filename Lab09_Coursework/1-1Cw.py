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
                agent_here=None
                if agents:
                    for a in agents:
                        if a.x==x and a.y==y:
                            agent_here=a
                            break
                if agent_here:row+=getattr(agent_here,'symbol','P')
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
        if not hasattr(self,'visited'):self.visited=set()
        if not hasattr(self,'target'):self.target=None
        self.visited.add((self.x,self.y))
        if self.target:
            tx,ty=self.target
            if self.x<tx:self.x+=1
            elif self.x>tx:self.x-=1
            elif self.y<ty:self.y+=1
            elif self.y>ty:self.y-=1
            if self.x==tx and self.y==ty:self.target=None
            return True
        moves=[(1,0),(0,1),(0,-1),(-1,0)]
        random.shuffle(moves)
        for dx,dy in moves:
            nx,ny=self.x+dx,self.y+dy
            if 0<=nx<env.width and 0<=ny<env.height:
                if (nx,ny) not in self.visited:
                    self.x=nx
                    self.y=ny
                    return True
        for y in range(env.height):
            for x in range(env.width):
                if (x,y) not in self.visited and env.grid[y][x]!=SEARCHED:
                    self.target=(x,y)
                    return True
        return False

class Human(Agent):
    def __init__(self,name,x,y):
        super().__init__(name,x,y)
        self.symbol='P'

class K9(Agent):
    def __init__(self,name,x,y):
        super().__init__(name,x,y)
        self.symbol='D'

class Bloodhound(Agent):
    def __init__(self,name,x,y):
        super().__init__(name,x,y)
        self.symbol='B'

async def main():
    env=Environment(300,13)
    pos=env.place_casualty(299,7)
    agents=[Human("person1",10,3),Human("person2",10,6),Human("person3",10,9),K9("rex",5,5),Bloodhound("max",5,7)]    
    found=False
    while not found:
        env.clear_screen()
        highlights=[]
        for a in agents:
            highlights+=a.get_view_cone(env)
        env.display(agents,highlights)
        for a in agents:
            if a.search(env):
                found=True
                break
            a.move_random(env)
        await asyncio.sleep(0.05)

if __name__=="__main__":
    asyncio.run(main())