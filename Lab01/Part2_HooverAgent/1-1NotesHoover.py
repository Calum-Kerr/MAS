#!/usr/bin/env python3

import asyncio, random

#location = ?
#grid = ?

class Agent():
    async def run(self):
        global location, grid
        while True:
            #?
            await asyncio.sleep(1)

async def environment():
    while True:
        #?
        await asyncio.sleep(1)

async def main():
    agent = Agent()
    await asyncio.gather(environment(),agent.run())

if __name__ == "__main__":
    asyncio.run(main())