#!/usr/bin/env python3

import asyncio, random

location = 0
garden=[0]*10
for i in range(5):
    position=random.randint(0,9)
    garden[position]=random.randint(1,5)

class Agent():
    async def run(self):
        global garden, location
        while True:
            if garden[location] > 0:
                garden[location] = garden[location]-1
                print("a flower grew here and nectar was collected!")
            else:
                print("nothing grew and no nectar is here")
            location = (location+1)%len(garden)
            await asyncio.sleep(1)

async def environment():
    while True:
        print(f"[environment]{location}")
        print(f"[environment]{garden}")
        await asyncio.sleep(1)

async def main():
    agent = Agent()
    await asyncio.gather(environment(),agent.run())

if __name__=="__main__":
    asyncio.run(main())