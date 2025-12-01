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

def english_auction(starting_price, agents):
    current_price=starting_price
    current_winner=None
    bidding=True
    round_num=0
    while bidding:
        round_num += 1
        bidding=False
        for agent in agents:
            bid = agent.make_bid(current_price)
            if bid:
                current_price = bid
                current_winner = agent
                bidding=True
        print(f"Round {round_num}: Current price {current_price}, Current winner {current_winner.name if current_winner else None}")
    return current_winner, current_price

def main():

if __name__=="__main__":
    asyncio.run(main())