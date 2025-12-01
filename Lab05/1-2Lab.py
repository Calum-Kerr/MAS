#!/usr/bi/env python3


import asyncio,uuid

class Directory():
    def __init__(self):
        self.agents={}
    def register(self,agent):
        self.agents[agent.uid]=agent
    def deregister(self,agent):
        if agent.uid in self._agents:
            del self.agents[agent.uid]
    def list_agents(self):
        return list(self._agent.values())
    def lookup(self,uid):
        return self.agents.get(uid,None)
    def contains(self,uid):
        return uid in self.agents

class Agent():
    def __init__(self,name=None):
        self.uid=uuid.uuid4()
        self.name=name if name else str(self.uid)
        self.alive=True
    async def run(self):
        while self.alive:
            print(f"agent{self.name} taking a turn")
            await asyncio.sleep(1)

async def main():
    agent1=Agent("calum")
    agent2=Agent("simon")
    await asyncio.gather(agent1.run(),agent2.run())

if __name__=="__main__":
    asyncio.run(main())