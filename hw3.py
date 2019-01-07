'''
Created on Sep 26, 2017

I pledge my honor that I abided by the Stevens Honor System. ytakezaw
@author: Yoshika Takezawa

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.
from cs115 import *
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here
def giveChange(amount, coins):
    ''' nonnegative amount of money, coin system being used[1,5,10,25,50]  [1, 7, 24, 42]
    returns the least number of coins to give as change
    counts the number of coins used
    min (x,y)
    returns as [number  of coins, [list of coins]]
    '''
    if amount == 0:
        return [0, []]
    if coins ==[] or amount < 0 or coins ==[0]:
        return [float("inf"), coins]
    if amount == coins[0]:
        return [1, [coins[0]]]
    if coins[0] > amount:
        return giveChange(amount, coins[1:])
    huh1 = giveChange(amount - coins[0], coins)
    new_sum = 1 + huh1[0]
    huh2 = giveChange(amount, coins[1:])
    if new_sum < huh2[0]:
        return [new_sum, [coins[0]]+ huh1[1]]
    return huh2 
print(giveChange(16, [1,2,3,4,5]))


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scorelist):
    '''takes in a letter and outputs the score associated with it.'''
    if letter == '':
        return 0
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])
#print(letterscore('z', scrabbleScores))

def wordScore(S, scorelist):
    '''takes in a string and returns the score for that string'''
    if S == '':
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)
#print(wordScore('apple', scrabbleScores))

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)
#print(wordsWithScore(Dictionary, scrabbleScores))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n== 0 or L == []:
        return []
    return [L[0]]+ take(n-1, L[1:])
    
#print(take(4, [0,1,2,3,4,5,6,7]))
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n == 0:
        return L
    if L == []:
        return []
    return drop(n-1, L[1:])
#print(drop(4, [0,1,2,3,4,5,6]))
    
    
    