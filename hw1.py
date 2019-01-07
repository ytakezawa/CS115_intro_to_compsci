'''
Created on Sep 9, 2017

@author: Yoshi
I pledge my honor that I abided by the Stevens Honor System.   ytakezaw
'''

'''notes 9/11/17 --Recursion is the process by which a function calls itself.
The base case is when no recursion is needed, that is, the output for a given input is known.
The recursive calls should alter the output as to gradually approach the input of the base case.
Each time a recursive call is made, the system pushes another stack frame in the call stack.
Once we reach the base case, we can return the result, thus popping the stack frame from the stack.
Finally, we will apply the result to the pending operation, 
and continue the process until we get to the top of the stack.'''

from cs115 import map, reduce

def mult(x, y):
    '''returns the product of x and y'''
    return x * y 

def factorial(n):
    '''input n and returns n! --> 1*2*3*4...*(n-1)*n'''
    return reduce(mult, range(1,n+1))


def add(x, y):
    '''returns the sum of x and y'''
    return x + y

def mean(L):
    '''take in a list and returns the average'''
    sumation = reduce(add,L)
    length= len(L)
    return float(sumation/length)

def divides(n):
    def div(k):
        return n % k == 0
    return div

def prime(n):
    '''checks if a number is prime. returns true if it is and false if it is not.
    (map(divides(n),range(1,n+1))) returns a list of Trues and Falses
    IDK ABOUT 1 SO FOR NOW IT IS NOT PRIME NUMBER'''
    if(reduce(add,(map(divides(n),range(1,n+1))))>2) or (n==1):
        return False
    return True