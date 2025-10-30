#!/usr/bin/env python3

import asyncio,random,uuid

won=False
winner=None
turn=0

blocks={'A':'table', 'B':'A', 'C':'B'}

goal_agent_x=
goal_agent_y=

class Agent():
    def __init__(self,player,goal):
        self.alive=True
        self.uid=uuid.uuid4()
        self.player=player
        self.goal=goal

    def is_clear(self,block):

    def act(self):

    async def run(self):
        


def environment():
    global turn
    print()
    print("turn " +str(turn))
    print_blocks()
    check_status()
    if (won):
        print()
        print('Agent '+winner+' has won!')
        print()
        stop_agents()
    elif turn>=20:
        print("Max turns have been played ... Draw!")
        stop_agents()
    turn = turn+1

def check_status():
    global winner, won

def stop_agents():
    tasks=asyncio.all_tasks()
    for task in tasks:
        task.cancel()

async def main():
    agent_x=Agent('x', goal_agent_x)
    agent_y=Agent('y', goal_agent_y)
    environment()
    try:
        await asyncio.gather(agent_x.run(), agent_y.run())
    except asyncio.CancelledError:
        print("Agents laid to rest..")

if __name__ =="__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print("Caught keboard interrupt. Stopping program!")