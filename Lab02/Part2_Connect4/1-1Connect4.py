#!/usr/bin/env python3

import asyncio, random, uuid

won=False
winner=None
turn=0
board=['-']*42

class Agent():
    def __init__(self, player):
        self.alive=True
        self.uid=uuid.uuid4()
        self.player=player
    def act(self):
        unplayed=[]
        for x in range(42):
            if board[x]=='-':
                unplayed.append(x)
        valid_moves=[]
        for pos in unplayed:
            col = pos % 7 
            row = pos // 7
            if row == 5 or board[pos + 7] != '-':
                valid_moves.append(pos)
        if self.player=='x':
            pos=random.choice(valid_moves)
        else :
            center=[38,31]
            pos=None
            for preferred in [center]:
                available=[p for p in preferred if p in valid_moves]
                if available:
                    pos=random.choice(available)
                    break
            if pos is None:
                pos=random.choice(valid_moves)
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
    elif(turn >=42):
        print("max number of turns reached and still no winner")
        stop_agents()
    turn=turn+1

def check_status():
    global winner, won
    if((board[0]=='x' and board[1]=='x' and board[2]=='x' and board[3]=='x')
       or
       (board[1]=='x' and board[2]=='x' and board[3]=='x' and board[4]=='x')
       or
       (board[2]=='x' and board[3]=='x' and board[4]=='x' and board[5]=='x')
       or
       (board[3]=='x' and board[4]=='x' and board[5]=='x' and board[6]=='x')
       or
       (board[7]=='x' and board[8]=='x' and board[9]=='x' and board[10]=='x')
       or
       (board[8]=='x' and board[9]=='x' and board[10]=='x' and board[11]=='x')
       or
       (board[9]=='x' and board[10]=='x' and board[11]=='x' and board[12]=='x')
       or
       (board[10]=='x' and board[11]=='x' and board[12]=='x' and board[13]=='x')
       or
       (board[14]=='x' and board[15]=='x' and board[16]=='x' and board[17]=='x')
       or
       (board[15]=='x' and board[16]=='x' and board[17]=='x' and board[18]=='x')
       or
       (board[16]=='x' and board[17]=='x' and board[18]=='x' and board[19]=='x')
       or
       (board[17]=='x' and board[18]=='x' and board[19]=='x' and board[20]=='x')
       or
       (board[21]=='x' and board[22]=='x' and board[23]=='x' and board[24]=='x')
       or
       (board[22]=='x' and board[23]=='x' and board[24]=='x' and board[25]=='x')
       or
       (board[23]=='x' and board[24]=='x' and board[25]=='x' and board[26]=='x')
       or
       (board[24]=='x' and board[25]=='x' and board[26]=='x' and board[27]=='x')
       or
       (board[28]=='x' and board[29]=='x' and board[30]=='x' and board[31]=='x')
       or
       (board[29]=='x' and board[30]=='x' and board[31]=='x' and board[32]=='x')
       or
       (board[30]=='x' and board[31]=='x' and board[32]=='x' and board[33]=='x')
       or
       (board[31]=='x' and board[32]=='x' and board[33]=='x' and board[34]=='x')
       or
       (board[35]=='x' and board[36]=='x' and board[37]=='x' and board[38]=='x')
       or
       (board[36]=='x' and board[37]=='x' and board[38]=='x' and board[39]=='x')
       or
       (board[37]=='x' and board[38]=='x' and board[39]=='x' and board[40]=='x')
       or
       (board[38]=='x' and board[39]=='x' and board[40]=='x' and board[41]=='x')
       or
       (board[0]=='x' and board[7]=='x' and board[14]=='x' and board[21]=='x')
       or
       (board[7]=='x' and board[14]=='x' and board[21]=='x' and board[28]=='x')
       or
       (board[14]=='x' and board[21]=='x' and board[28]=='x' and board[35]=='x')
       or
       (board[1]=='x' and board[8]=='x' and board[15]=='x' and board[22]=='x')
       or
       (board[8]=='x' and board[15]=='x' and board[22]=='x' and board[29]=='x')
       or
       (board[15]=='x' and board[22]=='x' and board[29]=='x' and board[36]=='x')
       or
       (board[2]=='x' and board[9]=='x' and board[16]=='x' and board[23]=='x')
       or
       (board[9]=='x' and board[16]=='x' and board[23]=='x' and board[30]=='x')
       or
       (board[16]=='x' and board[23]=='x' and board[30]=='x' and board[37]=='x')
       or
       (board[3]=='x' and board[10]=='x' and board[17]=='x' and board[24]=='x')
       or
       (board[10]=='x' and board[17]=='x' and board[24]=='x' and board[31]=='x')
       or
       (board[17]=='x' and board[24]=='x' and board[31]=='x' and board[38]=='x')
       or
       (board[4]=='x' and board[11]=='x' and board[18]=='x' and board[25]=='x')
       or
       (board[11]=='x' and board[18]=='x' and board[25]=='x' and board[32]=='x')
       or
       (board[18]=='x' and board[25]=='x' and board[32]=='x' and board[39]=='x')
       or
       (board[5]=='x' and board[12]=='x' and board[19]=='x' and board[26]=='x')
       or
       (board[12]=='x' and board[19]=='x' and board[26]=='x' and board[33]=='x')
       or
       (board[19]=='x' and board[26]=='x' and board[33]=='x' and board[40]=='x')
       or
       (board[6]=='x' and board[13]=='x' and board[20]=='x' and board[27]=='x')
       or
       (board[13]=='x' and board[20]=='x' and board[27]=='x' and board[34]=='x')
       or
       (board[20]=='x' and board[27]=='x' and board[34]=='x' and board[41]=='x')
       or
       (board[14]=='x' and board[22]=='x' and board[30]=='x' and board[38]=='x')
       or
       (board[7]=='x' and board[15]=='x' and board[23]=='x' and board[31]=='x')
       or
       (board[15]=='x' and board[23]=='x' and board[31]=='x' and board[39]=='x')
       or
       (board[0]=='x' and board[8]=='x' and board[16]=='x' and board[24]=='x')
       or
       (board[8]=='x' and board[16]=='x' and board[24]=='x' and board[32]=='x')
       or
       (board[16]=='x' and board[24]=='x' and board[32]=='x' and board[40]=='x')
       or
       (board[1]=='x' and board[9]=='x' and board[17]=='x' and board[25]=='x')
       or
       (board[9]=='x' and board[17]=='x' and board[25]=='x' and board[33]=='x')
       or
       (board[17]=='x' and board[25]=='x' and board[33]=='x' and board[41]=='x')
       or
       (board[2]=='x' and board[10]=='x' and board[18]=='x' and board[26]=='x')
       or
       (board[10]=='x' and board[18]=='x' and board[26]=='x' and board[34]=='x')
       or
       (board[3]=='x' and board[11]=='x' and board[19]=='x' and board[27]=='x')
       or
       (board[21]=='x' and board[15]=='x' and board[9]=='x' and board[3]=='x')
       or
       (board[28]=='x' and board[22]=='x' and board[16]=='x' and board[10]=='x')
       or
       (board[22]=='x' and board[16]=='x' and board[10]=='x' and board[4]=='x')
       or
       (board[35]=='x' and board[29]=='x' and board[23]=='x' and board[17]=='x')
       or
       (board[29]=='x' and board[23]=='x' and board[17]=='x' and board[11]=='x')
       or
       (board[23]=='x' and board[17]=='x' and board[11]=='x' and board[5]=='x')
       or
       (board[36]=='x' and board[30]=='x' and board[24]=='x' and board[18]=='x')
       or
       (board[30]=='x' and board[24]=='x' and board[18]=='x' and board[12]=='x')
       or
       (board[24]=='x' and board[18]=='x' and board[12]=='x' and board[6]=='x')
       or
       (board[37]=='x' and board[31]=='x' and board[25]=='x' and board[19]=='x')
       or
       (board[31]=='x' and board[25]=='x' and board[19]=='x' and board[13]=='x')
       or
       (board[38]=='x' and board[32]=='x' and board[26]=='x' and board[20]=='x')
       or
       (board[32]=='x' and board[26]=='x' and board[20]=='x' and board[14]=='x')
       or
       (board[39]=='x' and board[33]=='x' and board[27]=='x' and board[21]=='x')
       or
       (board[33]=='x' and board[27]=='x' and board[21]=='x' and board[15]=='x')
       or
       (board[40]=='x' and board[34]=='x' and board[28]=='x' and board[22]=='x')
       or
       (board[34]=='x' and board[28]=='x' and board[22]=='x' and board[16]=='x')
       or
       (board[41]=='x' and board[35]=='x' and board[29]=='x' and board[23]=='x')):
        winner='x'
        won=True
    elif((board[0]=='y' and board[1]=='y' and board[2]=='y' and board[3]=='y')
       or
       (board[1]=='y' and board[2]=='y' and board[3]=='y' and board[4]=='y')
       or
       (board[2]=='y' and board[3]=='y' and board[4]=='y' and board[5]=='y')
       or
       (board[3]=='y' and board[4]=='y' and board[5]=='y' and board[6]=='y')
       or
       (board[7]=='y' and board[8]=='y' and board[9]=='y' and board[10]=='y')
       or
       (board[8]=='y' and board[9]=='y' and board[10]=='y' and board[11]=='y')
       or
       (board[9]=='y' and board[10]=='y' and board[11]=='y' and board[12]=='y')
       or
       (board[10]=='y' and board[11]=='y' and board[12]=='y' and board[13]=='y')
       or
       (board[14]=='y' and board[15]=='y' and board[16]=='y' and board[17]=='y')
       or
       (board[15]=='y' and board[16]=='y' and board[17]=='y' and board[18]=='y')
       or
       (board[16]=='y' and board[17]=='y' and board[18]=='y' and board[19]=='y')
       or
       (board[17]=='y' and board[18]=='y' and board[19]=='y' and board[20]=='y')
       or
       (board[21]=='y' and board[22]=='y' and board[23]=='y' and board[24]=='y')
       or
       (board[22]=='y' and board[23]=='y' and board[24]=='y' and board[25]=='y')
       or
       (board[23]=='y' and board[24]=='y' and board[25]=='y' and board[26]=='y')
       or
       (board[24]=='y' and board[25]=='y' and board[26]=='y' and board[27]=='y')
       or
       (board[28]=='y' and board[29]=='y' and board[30]=='y' and board[31]=='y')
       or
       (board[29]=='y' and board[30]=='y' and board[31]=='y' and board[32]=='y')
       or
       (board[30]=='y' and board[31]=='y' and board[32]=='y' and board[33]=='y')
       or
       (board[31]=='y' and board[32]=='y' and board[33]=='y' and board[34]=='y')
       or
       (board[35]=='y' and board[36]=='y' and board[37]=='y' and board[38]=='y')
       or
       (board[36]=='y' and board[37]=='y' and board[38]=='y' and board[39]=='y')
       or
       (board[37]=='y' and board[38]=='y' and board[39]=='y' and board[40]=='y')
       or
       (board[38]=='y' and board[39]=='y' and board[40]=='y' and board[41]=='y')
       or
       (board[0]=='y' and board[7]=='y' and board[14]=='y' and board[21]=='y')
       or
       (board[7]=='y' and board[14]=='y' and board[21]=='y' and board[28]=='y')
       or
       (board[14]=='y' and board[21]=='y' and board[28]=='y' and board[35]=='y')
       or
       (board[1]=='y' and board[8]=='y' and board[15]=='y' and board[22]=='y')
       or
       (board[8]=='y' and board[15]=='y' and board[22]=='y' and board[29]=='y')
       or
       (board[15]=='y' and board[22]=='y' and board[29]=='y' and board[36]=='y')
       or
       (board[2]=='y' and board[9]=='y' and board[16]=='y' and board[23]=='y')
       or
       (board[9]=='y' and board[16]=='y' and board[23]=='y' and board[30]=='y')
       or
       (board[16]=='y' and board[23]=='y' and board[30]=='y' and board[37]=='y')
       or
       (board[3]=='y' and board[10]=='y' and board[17]=='y' and board[24]=='y')
       or
       (board[10]=='y' and board[17]=='y' and board[24]=='y' and board[31]=='y')
       or
       (board[17]=='y' and board[24]=='y' and board[31]=='y' and board[38]=='y')
       or
       (board[4]=='y' and board[11]=='y' and board[18]=='y' and board[25]=='y')
       or
       (board[11]=='y' and board[18]=='y' and board[25]=='y' and board[32]=='y')
       or
       (board[18]=='y' and board[25]=='y' and board[32]=='y' and board[39]=='y')
       or
       (board[5]=='y' and board[12]=='y' and board[19]=='y' and board[26]=='y')
       or
       (board[12]=='y' and board[19]=='y' and board[26]=='y' and board[33]=='y')
       or
       (board[19]=='y' and board[26]=='y' and board[33]=='y' and board[40]=='y')
       or
       (board[6]=='y' and board[13]=='y' and board[20]=='y' and board[27]=='y')
       or
       (board[13]=='y' and board[20]=='y' and board[27]=='y' and board[34]=='y')
       or
       (board[20]=='y' and board[27]=='y' and board[34]=='y' and board[41]=='y')
       or
       (board[14]=='y' and board[22]=='y' and board[30]=='y' and board[38]=='y')
       or
       (board[7]=='y' and board[15]=='y' and board[23]=='y' and board[31]=='y')
       or
       (board[15]=='y' and board[23]=='y' and board[31]=='y' and board[39]=='y')
       or
       (board[0]=='y' and board[8]=='y' and board[16]=='y' and board[24]=='y')
       or
       (board[8]=='y' and board[16]=='y' and board[24]=='y' and board[32]=='y')
       or
       (board[16]=='y' and board[24]=='y' and board[32]=='y' and board[40]=='y')
       or
       (board[1]=='y' and board[9]=='y' and board[17]=='y' and board[25]=='y')
       or
       (board[9]=='y' and board[17]=='y' and board[25]=='y' and board[33]=='y')
       or
       (board[17]=='y' and board[25]=='y' and board[33]=='y' and board[41]=='y')
       or
       (board[2]=='y' and board[10]=='y' and board[18]=='y' and board[26]=='y')
       or
       (board[10]=='y' and board[18]=='y' and board[26]=='y' and board[34]=='y')
       or
       (board[3]=='y' and board[11]=='y' and board[19]=='y' and board[27]=='y')
       or
       (board[21]=='y' and board[15]=='y' and board[9]=='y' and board[3]=='y')
       or
       (board[28]=='y' and board[22]=='y' and board[16]=='y' and board[10]=='y')
       or
       (board[22]=='y' and board[16]=='y' and board[10]=='y' and board[4]=='y')
       or
       (board[35]=='y' and board[29]=='y' and board[23]=='y' and board[17]=='y')
       or
       (board[29]=='y' and board[23]=='y' and board[17]=='y' and board[11]=='y')
       or
       (board[23]=='y' and board[17]=='y' and board[11]=='y' and board[5]=='y')
       or
       (board[36]=='y' and board[30]=='y' and board[24]=='y' and board[18]=='y')
       or
       (board[30]=='y' and board[24]=='y' and board[18]=='y' and board[12]=='y')
       or
       (board[24]=='y' and board[18]=='y' and board[12]=='y' and board[6]=='y')
       or
       (board[37]=='y' and board[31]=='y' and board[25]=='y' and board[19]=='y')
       or
       (board[31]=='y' and board[25]=='y' and board[19]=='y' and board[13]=='y')
       or
       (board[38]=='y' and board[32]=='y' and board[26]=='y' and board[20]=='y')
       or
       (board[32]=='y' and board[26]=='y' and board[20]=='y' and board[14]=='y')
       or
       (board[39]=='y' and board[33]=='y' and board[27]=='y' and board[21]=='y')
       or
       (board[33]=='y' and board[27]=='y' and board[21]=='y' and board[15]=='y')
       or
       (board[40]=='y' and board[34]=='y' and board[28]=='y' and board[22]=='y')
       or
       (board[34]=='y' and board[28]=='y' and board[22]=='y' and board[16]=='y')
       or
       (board[41]=='y' and board[35]=='y' and board[29]=='y' and board[23]=='y')):
        winner='y'
        won=True

def print_board():
    print(board[0]+'|'+board[1]+'|'+board[2]+'|'+board[3]+'|'+board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9]+'|'+board[10]+'|'+board[11]+'|'+board[12]+'|'+board[13])
    print(board[14]+'|'+board[15]+'|'+board[16]+'|'+board[17]+'|'+board[18]+'|'+board[19]+'|'+board[20])
    print(board[21]+'|'+board[22]+'|'+board[23]+'|'+board[24]+'|'+board[25]+'|'+board[26]+'|'+board[27])
    print(board[28]+'|'+board[29]+'|'+board[30]+'|'+board[31]+'|'+board[32]+'|'+board[33]+'|'+board[34])
    print(board[35]+'|'+board[36]+'|'+board[37]+'|'+board[38]+'|'+board[39]+'|'+board[40]+'|'+board[41])

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