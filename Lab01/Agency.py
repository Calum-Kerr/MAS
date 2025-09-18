#!/usr/bin/env python3

import asyncio
import random

temp=20

class Agent():
    async def run(self):
        while True:
            if temp >= 20:
                print("The temperature is sweet")
            else: 
                print("The temperature is bad!!")
            await asyncio.sleep(1)

async def environment():
    global temp
    while True:
        temp = random.randrange(12,28)
        print(temp)
        await asyncio.sleep(1)

async def main():
    agent = Agent()
    await asyncio.gather(environment(),agent.run())

if __name__ == "__main__":
    asyncio.run(main())
