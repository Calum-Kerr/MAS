#!/usr/bin/env python3

import asyncio, random

location = 0
garden = [0,3,0,5,2,0,4,0,1,0]

class Agent():
    async def run(self):
        global location, garden
        while True:
            if garden[location] > 0:
                garden[location] = garden[location]-1
                print("nectar is collected")
            else:
                print("no flower here!")
            location = (location+1)%len(garden)
            await asyncio.sleep(1)

async def environment():
    while True:
        print(f"[Environment] {location}")
        print(f"[environment] {garden}")
        await asyncio.sleep(1)

async def main():
    agent = Agent()
    await asyncio.gather(environment(),agent.run())

if __name__ =="__main__":
    asyncio.run(main())