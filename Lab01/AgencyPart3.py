#!/usr/bin/env python

import asyncio, random

temp=20
heater=False

class Agent():
    async def run(Self):
        global heater
        while True:
            if temp < 20:
                heater = True
                print("heater is running")
            else:
                heater = False
                print("heater has switched off")
            await asyncio.sleep(1)

async def environment():
    while True:
        global temp 
        #temp = random.randrange(18,22)
        if heater:
            temp += random.randint(1,3)
        else:
            temp -= random.randint(1,1)
        print(f"[Environment] Temp: {temp}")
        await asyncio.sleep(1)

async def main():
    agent = Agent()
    await asyncio.gather(environment(),agent.run())

if __name__ == "__main__":
    asyncio.run(main())