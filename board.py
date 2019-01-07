'''
Created on Nov 30, 2017

I pledge my honor that I have abided by the Stevens Honor System. ytakezaw

THE CONNECT FOUR GAME LAST HW!!!

@author: Yoshika Takezawa
'''
import sys

class Board(object):
    '''three data members: there will be a two-dimensional list
    (a list of lists) containing characters to represent the game area, and a pair of variables holding the
    number of rows and columns on the board (6 rows and 7 columns is standard)'''
    def __init__(self, cols = 7, rows= 6):
        self.cols = cols 
        self.rows = rows
        self.theboard = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    def __str__(self):
        '''displays board'''
        brd= ''
        for r in range(int(self.rows)):
            for c in range(int(self.cols)):
                if c == int(self.cols)-1:
                    brd += '|' + self.theboard[r][c] +'|\n'
                else:
                    brd += '|' + self.theboard[r][c]
        brd += self.cols * '--' +'\n'
        for i in range(int(self.cols)):
            brd += ' ' + str(i)
        return brd
    
    def allowsMove(self, col):
        '''determines is move is valid'''
        try:
            for r in range(int(self.rows)):
                if self.theboard[r][col] == ' ':
                    return True
        except:
                return False
    
    def addMove(self, col, ox):
        '''player adds O or X in col'''
        x= int(self.rows) -1
        if self.allowsMove(int(col)) == True:
            while self.theboard[x][col] != ' ':
                x -= 1
            if self.theboard[x][col] == ' ':
                self.theboard[x][col] = ox
        #print(self.theboard)
        
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'
        
        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers
        """
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.cols:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
    def delMove(self, col):
        '''removes the top checker in the column
        if no checker, does nothing'''
        for r in range(int(self.rows)):
            if self.theboard[r][col] != ' ':
                self.theboard[r][col] = ' '
                break
    
    def winsFor(self, ox):
        '''returns true if given ox won (horizontally, vertically, or diagonal(2))
        returns false otherwise'''
        '''checks horizontally'''
        for r in range(int(self.rows)):
            for c in range(int(self.cols)):
                try:
                    if (self.theboard[r][c]==ox) and (self.theboard[r][c+1]==ox) and \
                    (self.theboard[r][c+2]==ox) and (self.theboard[r][c+3]==ox):
                        return True
                except:
                    pass
                
        '''checks vertically'''
        for r in range(int(self.rows)):
            for c in range(int(self.cols)):
                try:
                    if (self.theboard[r][c]==ox) and (self.theboard[r+1][c]==ox) and \
                    (self.theboard[r+2][c]==ox) and (self.theboard[r+3][c]==ox):
                        return True
                except:
                    pass
                
        '''checks diagonally /'''
        for r in range(int(self.rows)):
            for c in range(int(self.cols)):
                try:
                    if (self.theboard[r][c]==ox) and (self.theboard[r+1][c-1]==ox) and \
                    (self.theboard[r+2][c-2]==ox) and (self.theboard[r+3][c-3]==ox):
                        return True
                except:
                    pass
                
        '''checks diagonally (\)'''
        for r in range(int(self.rows)):
            for c in range(int(self.cols)):
                try:
                    if (self.theboard[r][c]==ox) and (self.theboard[r+1][c+1]==ox) and \
                    (self.theboard[r+2][c+2]==ox) and (self.theboard[r+3][c+3]==ox):
                        return True
                except: 
                    pass
        return False
    
    def hostGame(self):
        '''Runs a loop to allow the players to play a game of connect four'''
        print("Welcome to Connect Four!")
        print(self)
        ox = 'O'
        while self.winsFor(ox)==False:
            if ox == 'O':
                ox = 'X'
                move = input("X's choice:")
                while self.allowsMove(int(move)) == False:
                    move = input("X's choice:")
                self.addMove(int(move), ox)
            elif ox == 'X':
                ox = 'O'
                move = input("O's choice:")
                while self.allowsMove(int(move)) == False:
                    move = input("O's choice:")
                self.addMove(int(move), ox)
            print(self)
        print(ox + " wins -- Congratulations!")
        sys.exit()
        
                
        
s= Board(7,6)
s.hostGame()