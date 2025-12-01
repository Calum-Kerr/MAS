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
    
def dutch_auction(agents, starting_price=200,decrement=17):
    current_price=starting_price
    round_num=0
    while current_price > 0:
        round_num += 1
        for agent in agents:
            if agent.will_bid(current_price):
                print(f"Round {round_num}: {agent.name} bids {current_price}")
                return agent, current_price
        current_price -= decrement
        print(f"Round {round_num}: Current price {current_price}")
    print("Auction over")
    return None,0

def main():
    agents = [Agent("calum", 100), Agent("simon", 150), Agent("jim", 120)]
    dutch_auction(agents,200)

if __name__=="__main__":
    main()