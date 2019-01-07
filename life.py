#
# life.py - Game of Life lab
#
# Name: Yoshika Takezawa
# Pledge: I pledge that I have abided by the Stevens Honor System. ytakezaw
#

import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A
A = createBoard(5, 3)
#print(A)

import sys
def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
#printBoard(A)

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A
#A = diagonalize(7,6)
#printBoard(A)

def innerCells(w, h):
    ''' creates an empty board and then modifies it 
    so that it has 'on' cells in the inside'''
    A = createBoard(w, h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = 1
    return A
#A = innerCells(7,6)
#printBoard(A)

def randomCells(w, h):
    '''  returns an array of randomly-assigned 1's
    and 0's except that the outer edge of the array 
    is still completely empty (all 0's)'''
    A = createBoard(w, h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = random.choice( [0,1] )
    return A
#A = randomCells(7,6)
#printBoard(A)

#oldA = createBoard(2,2) # create a 2x2 empty board
#printBoard(oldA) # show it
#newA = oldA # create a false ("shallow") copy 
#printBoard(newA) # show it
#oldA[0][0] = 1 # set oldA's upper left corner to 1
#printBoard(oldA) # the upper left will be 1
#printBoard(newA) # but newA has changed, too!!


def copy(A):
    '''makes a deep copy of A'''
    new= []
    for i in A:
        if isinstance(i, list):
            new.append(copy(i))
        else:
            new.append(i)
    return new
# oldA = createBoard(2,2)
# #printBoard(oldA)
# newA = copy( oldA )
# #printBoard(newA)
# oldA[0][0] = 1
# printBoard(oldA)
# printBoard(newA)

def innerReverse(A):
    ''' takes an old 2d array (or "generation") and then
    creates a new generation of the same shape and size'''
    w=len(A[0])
    h=len(A)
    newA =copy(A)
    for row in range(1, h-1):
        for col in range(1, w-1):
            if newA[row][col] == 1:
                newA[row][col]= 0
            else:
                newA[row][col]=1
    return newA
#A = randomCells(8,8)
#printBoard(A)
# A2 = innerReverse(A)
# printBoard(A2)

def countNeighbors( row, col, A ):
    '''counts how many neighbors for a given cell'''
    count = 0
    for x in range(-1,2,1):
        for y in range(-1, 2, 1):
            if abs(x) + abs(y) != 0:
                count += A[row+x][col+y]
    return count
#print(countNeighbors(3,3, A))

def next_life_generation( A ):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    w=len(A[0])
    h=len(A)
    newA =copy(A)
    for x in range(h):
        for y in range(w):
            if 0 < x < h-1 and 0 < y < w-1:
                count = countNeighbors(x, y, A)
                if count < 2 or count > 3:
                    newA[x][y] = 0
                elif count == 3:
                    newA[x][y] = 1
                else:
                    newA[x][y] = A[x][y]
            else:
                newA[x][y] = 0
    return newA

# A = [ [0,0,0,0,0],
# [0,0,1,0,0],
# [0,0,1,0,0],
# [0,0,1,0,0],
# [0,0,0,0,0]]
# printBoard(A)
# A2 = next_life_generation( A )
# printBoard(A2)
# A3 = next_life_generation( A2 )
# printBoard(A3)