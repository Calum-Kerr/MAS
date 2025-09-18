#!/usr/bin/env python3

import asyncio, random

temp=20
heater=False #we have the heater off by default

class Agent():
    async def run(self):
        global heater 
        while True:
            if temp < 20: 
                heater = True
                print("heater is running")
            else:
                heater = False
                print("heater is off")
            await asyncio.sleep(1)

async def environment():
    while True:
        global temp
        temp = random.randrange(19,21)
        print(temp)
        await asyncio.sleep(1)

async def main():
    agent =Agent()
    await asyncio.gather(environment(),agent.run())

if __name__=="__main__":
    asyncio.run(main())