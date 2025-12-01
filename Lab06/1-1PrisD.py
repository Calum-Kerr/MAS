#!/usr/bi/env python3


import asyncio,uuid,random

payoff_matrix={'defect':{'defect':(2,2),'cooperate':(5,0)},'cooperate':{'defect':(0,5),'cooperate':(3,3)}}

class Agent():
    def __init__(self,name=None, strategy=random):
        self.uid=uuid.uuid4()
        self.name=name if name else str(self.uid)
        self.strategy=strategy
        self.score=0
    def choose_action(self):
        if self.strategy == random:
            return random.choice(['defect','cooperate'])
        else:
            return self.strategy
    async def run(self):
        while self.alive:
            print(f"agent{self.name} taking a turn")
            await asyncio.sleep(1)

def play_game(strategy1, strategy2):
    action1 = strategy1.choose_action()
    action2 = strategy2.choose_action()
    payoff1, payoff2 = payoff_matrix[strategy1][strategy2]
    strategy1.score += payoff1
    strategy2.score += payoff2
    print(f"agent1 chose {action1} and agent2 chose {action2}")
    print(f"agent1 score: {strategy1.score} and agent2 score: {strategy2.score}")
    print()
    return payoff1, payoff2

async def main():
    agent1=Agent("calum")
    agent2=Agent("simon")
    await asyncio.gather(agent1.run(),agent2.run())

if __name__=="__main__":
    asyncio.run(main())