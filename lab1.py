'''
Created on Sep 7, 2017

@author: Yoshi
I pledge my honor that I have abided by the STevens honor system. ytakezaw
'''
from cs115 import map, reduce
import math


def inverse(n):
    '''returns inverse of n'''
    return float(1/n)

def e(n):
    '''1 + 1/1! + 1/2! +... takes the range and gets factorials of all of them. 
    then inverses them all. and add all of them up +1 '''
    return float(sum(map (inverse,map(math.factorial,range(1,n+1)))) + 1)

def error(n):
    '''finds difference between e and our def of e'''
    return float(abs(math.e-e(n)))
