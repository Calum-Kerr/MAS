#!/usr/bin/env python3

import asyncio,random,uuid

won=False
winner=None
turn=0

blocks={'A':'table', 'B':'table','C':'table'}

goal_agent_x={'A':'table','B':'A','C':'B'}
goal_agent_y={'B':'table','C':'B','A':'C'}

class Agent():
    def __init__(self,player,goal):
        self.alive=True
        self.uid=uuid.uuid4()
        self.player=player
        self.goal=goal
    def is_clear(self,block):
        return block not in blocks.values() or all(blocks[b]!=block for b in blocks)
    def act(self):
        for block, goal_location in self.goal.items():
            if blocks[block]!=goal_location and self.is_clear(block):
                if goal_location!='table' and not self.is_clear(goal_location):
                    continue
                opponent_goal=goal_agent_y if self.player=='x'else goal_agent_x
                if blocks[block]==opponent_goal.get(block):
                    continue
                blocks[block]=goal_location
                return True
        return False
    async def run(self):
        while self.alive:
            try:
                await asyncio.sleep(1)
            except asyncio.CancelledError:
                print("stopping all agents and cleaning up")
                raise

def environment():
    global turn
    print()
    print("turn " +str(turn))
    print_blocks()
    check_status()
    if turn%2==0:
        agent_x.act()
        print(f"agent x moved")
    else:
        agent_y.act()
        print(f"Agent y moved")
    if (won):
        print()
        print('Agent '+winner+' has won!')
        print()
        stop_agents()
    elif turn>=20:
        print("Max turns have been played ... Draw!")
        stop_agents()
    turn = turn+1

def print_blocks():
    print(f"blocks agent: {blocks}")
    print(f"agent x goal (abc stack): {goal_agent_x}")
    print(f"agent y goal (bca stack): {goal_agent_y}")

def check_status():
    global winner, won
    if blocks==goal_agent_x:
        winner='x'
        won=True
    elif blocks==goal_agent_y:
        winner='y'
        won=True

def stop_agents():
    tasks=asyncio.all_tasks()
    for task in tasks:
        task.cancel()

async def main():
    global agent_x, agent_y
    agent_x=Agent('x', goal_agent_x)
    agent_y=Agent('y', goal_agent_y)
    async def env_loop():
        while True:
            environment()
            await asyncio.sleep(1)
    try:
        await asyncio.gather(agent_x.run(), agent_y.run(), env_loop())
    except asyncio.CancelledError:
        print("Agents laid to rest..")

if __name__ =="__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print("Caught keboard interrupt. Stopping program!")