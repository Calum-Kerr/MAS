#!/usr/bin/env python3

import asyncio, random, uuid

won=False
winner=None
turn=0
board=['-']*9

class Agent():
    def __init__(self, player):
        self.alive=True
        self.uid=uuid.uuid4()
        self.player=player
    def act(self):
        unplayed=[]
        for x in range(9):
            if board[x]=='-':
                unplayed.append(x)
        pos=random.choice(unplayed)
        board[pos]=self.player
    async def run(self):
        while True:
            self.act()
            environment()
            try:
                await asyncio.sleep(1)
            except asyncio.CancelledError as e:
                print("Stopping agents and cleaning up")
                raise

def environment():
    global turn
    print()
    print("turn " +str(turn))
    print_board()
    check_status()
    if(won):
        print()
        print('player '+winner+' has won!')
        print()
        stop_agents()
    elif(turn >=9):
        print("max number of turns reached and still no winner")
        stop_agents()
    turn=turn+1

def check_status():
    global winner, won
    if((board[0]=='x' and board[1]=='x' and board[2]=='x')
       or
       (board[3]=='x' and board[4]=='x' and board[5]=='x')
       or
       (board[6]=='x' and board[7]=='x' and board[8]=='x')
       or
       (board[0]=='x' and board[3]=='x' and board[6]=='x')
       or
       (board[1]=='x' and board[4]=='x' and board[7]=='x')
       or
       (board[2]=='x' and board[5]=='x' and board[8]=='x')
       or
       (board[0]=='x' and board[4]=='x' and board[8]=='x')
       or
       (board[2]=='x' and board[4]=='x' and board[6]=='x')):
        winner='x'
        won=True
    elif((board[0]=='y' and board[1]=='y' and board[2]=='y')
       or
       (board[3]=='y' and board[4]=='y' and board[5]=='y')
       or
       (board[6]=='y' and board[7]=='y' and board[8]=='y')
       or
       (board[0]=='y' and board[3]=='y' and board[6]=='y')
       or
       (board[1]=='y' and board[4]=='y' and board[7]=='y')
       or
       (board[2]=='y' and board[5]=='y' and board[8]=='y')
       or
       (board[0]=='y' and board[4]=='y' and board[8]=='y')
       or
       (board[2]=='y' and board[4]=='y' and board[6]=='y')):
        winner='y'
        won=True

def print_board():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])

def stop_agents():
    tasks=asyncio.all_tasks()
    for task in tasks:
        task.cancel()

async def main():
    agent1=Agent('x')
    agent2=Agent('y')
    environment()
    try:
        await asyncio.gather(agent1.run(),agent2.run())
    except asyncio.CancelledError:
        print("agents laid to rest..")

if __name__=="__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print("caught keyboard interrut. stopping program.")