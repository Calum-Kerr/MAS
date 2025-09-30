#!/usr/bin/env python3

import asyncio, random

location = 0
grid = [True, False, True, False, True]

class Agent():
    async def run(self):
        global location, grid
        while True:
            if grid[location] == True:
                grid[location] = False
                print("cleaned")
            else:
                print("already clean")
            location = (location+1) %len(grid)
            await asyncio.sleep(1)

async def environment():
    while True:
        print(f"[environment] {grid}")
        print(f"[environment] {location}")
        await asyncio.sleep(1)

async def main():
    agent = Agent()
    await asyncio.gather(environment(),agent.run())

if __name__ == "__main__":
    asyncio.run(main())