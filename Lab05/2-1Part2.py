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
    
directory=Directory()

class MessageSystem():
    def __init__(self):
        self._queues={}
    def create_queue(self,uid):
        self._queues[uid]=[]
    def send(self,recipient_uid,message):
        if recipient_uid in self._queues:
            self._queues[recipient_uid].append(message)
    def receive(self,uid):
        if uid in self._queues and len(self._queues[uid])>0:
            return self._queues[uid].pop(0)
        return None
    def receive_all(self,uid):
        if uid in self._queues:
            messages=self._queues[uid].copy()
            self._queues[uid]=[]
            return messages
        return []

messages=MessageSystem()

class Agent():
    def __init__(self,name=None):
        self.uid=uuid.uuid4()
        self.name=name if name else str(self.uid)
        self.alive=True
        directory.register(self)
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