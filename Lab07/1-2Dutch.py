#!/usr/bin/env python3

import asyncio,random,uuid

class Agent():
    def __init__(self,name=None,valuation=0):
        self.uid=uuid.uuid4()
        self.name=name if name else str(self.uid)[:8]
        self.valuation=valuation
    def make_bid(self, current_price, increment=1):
        new_bid = current_price + increment
        if new_bid <= self.valuation:
            return new_bid
        else:
            return None
    def will_bid(self, current_price):
        return current_price <= self.valuation

def main():
    agents = [Agent("calum", 100), Agent("simon", 150), Agent("jim", 120)]

if __name__=="__main__":
    main()