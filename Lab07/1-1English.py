#!/usr/bin/env python3

import asyncio,random,uuid

class Agent():
    def __init__(self,name=None,valuation=0):
        self.uid=uuid.uuid4()
        self.name=name if name else str(self.uid)[:8]
        self.valuation=valuation

def make bid():

def english_auction():

def main():

if __name__=="__main__":
    asyncio.run(main())