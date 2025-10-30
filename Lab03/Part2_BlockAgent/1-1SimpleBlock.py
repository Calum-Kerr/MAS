#!/usr/bin/env python3

import asyncio,random

block_state={'a':'table','b':'table','c':'table'}

class Agent():
    async def run(self):
        global block_state
        while True:
            all_blocks=['a','b','c']
            block_to_move=random.choice(all_blocks)
            destination=random.choice(['table'])
            block_state[block_to_move]=destination
            print(f"moved: {block_to_move} onto {destination}")
            await asyncio.sleep(1)

async def main():
    agent=Agent()
    await asyncio.gather(agent.run())

if __name__=="__main__":
    asyncio.run(main())