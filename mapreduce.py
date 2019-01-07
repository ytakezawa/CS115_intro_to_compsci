'''
Created on Sep 7, 2017

@author: Yoshi
'''
from cs115 import range, map, reduce

def add(a,b):
    return a+b

def sqr(x):
    return x*x

def mult(a,b):
    return a*b

def span(lst):
    return reduce(max, lst)-reduce (min, lst)

def gauss(n):
    return reduce(add,range(1, n+1))

def sum_of_squares(n):
    return reduce(add, map(sqr, range(1, n+1)))
                           
list_of_strings = ['hello', 'my', 'name', 'is', 'yoshi']
print (map(len, list_of_strings))

list_of_ints = [1,2,3,4,5]
print(reduce (mult,list_of_ints))

print (span([3,1,42,7,-1]))
print (gauss(10))
print (sum_of_squares(10))

