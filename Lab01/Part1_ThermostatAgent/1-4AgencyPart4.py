#!/usr/bin/env python3

import asyncio, random
temp=10
heater=False
weather="cold"

class Agent():
    async def run(self):
        global heater
        while True:
            if temp < 20:
                heater = True
                print("heater is running")
            else:
                heater =False
                print("heater has turned off")
            await asyncio.sleep(1)

async def environment():
    global temp, heater, weather
    while True:
        if weather == "cold":
            if heater :
                temp += random.randint(1,3)
            else:
                temp -= random.randint(1,2)
        print(f"[environment] temp:{temp}")
        await asyncio.sleep(1)

async def main():
    agent = Agent()
    await asyncio.gather(environment(),agent.run())

if __name__ == "__main__":
    asyncio.run(main())