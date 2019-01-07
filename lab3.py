'''
Created on Sep 21, 2017

I pledge my honor that I abided by the Stevens Honor System. ytakezaw

@author: Yoshika Takezawa
'''
from cs115 import *

def change(amount, coins):
    ''' nonnegative amount of money, coin system being used[1,5,10,25,50]  [1, 7, 24, 42]
    returns the least number of coins to give as change
    counts the number of coins used
    min (x,y)
    '''
    if amount == 0:
        return 0
    if coins ==[] or amount < 0:
        return float("inf")
    if amount == coins[0]:
        return 1
    if coins[0] > amount:
        return change(amount, coins[1:])
    return min(1 + change(amount - coins[0], coins), change(amount, coins[1:]) )
print(change(15, [1, 5, 10, 20, 50]))