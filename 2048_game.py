from tkinter import *
from tkinter import messagebox
import random


class Board:
    def __init__(self):
        self.n=4
        self.window=Tk()
        self.window.title('2048 Game')
        self.gameArea=Frame(self.window,bg= 'azure3')
        self.board=[]
        self.gridCell=[[0]*4 for i in range(4)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0
        for i in range(4):
            rows=[]
            for j in range(4):
                l=Label(self.gameArea,text='',bg='azure4',
                font=('arial',22,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)
                rows.append(l);
            self.board.append(rows)
        self.gameArea.grid()
    def reverse(self):
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                i+=1
                j-=1
    def transpose(self):
        self.gridCell=[list(t)for t in zip(*self.gridCell)]


class Game:
    def __init__(self,gamepanel):
        self.gamepanel=gamepanel
        self.end=False
        self.won=False
    def start(self):
        self.gamepanel.random_cell()
        self.gamepanel.random_cell()
        self.gamepanel.paintGrid()
        self.gamepanel.window.bind('<Key>', self.link_keys)
        self.gamepanel.window.mainloop()
gamepanel =Board()
game2048 = Game( gamepanel)
game2048.start()