'''
Created on Sep 14, 2017

@author: Yoshika Takezawa

I pledge my honor that I abided by the Stevens Honor System. ytakezaw
'''

def dot(L, K):
    '''multiplies the items in the same position in each vector and adds the next set of products'''
    def dot_helper(L, K, accum):
        if L ==[] or K ==[]:
            return accum
        return dot_helper(L[1:], K[1:], L[0]*K[0]+ accum)
    return dot_helper(L, K, 0)
print (dot([5, 3], [6]))


def explode(S):
    ''' takes a string and outputs a list of characters
    easy way out is to use list(S), but how does it work?
    S[0] + S[1]+ S[2]+...returns 012...
    we want to make them into separate strings, separate objects
    '''
    if S=='':
        return []
    return [S[0]]+explode(S[1:])
print (explode('hello'))


def ind(e,L):
    '''returns the index where e is first found in L'''
    
    if L=='' or L==[]:
        return 0
    if e==L[0]:
        return 0
    return 1+ ind(e, L[1:])
print(ind('hi', ['hello', 42, True]))


def removeAll(e,L):
    '''takes in a list of numbers (L) and takes out any numbers==e and
    outputs that list of numbers without e'''
    def removeAll_helper(e,L,accum):
        if L==[]:
            return accum
        if e==L[0]:
            return removeAll_helper (e, L[1:], accum)
        return removeAll_helper(e,L[1:],accum + L[0:1])
    return removeAll_helper(e, L,[])
print(removeAll([77, 42], [55, [77, 42], [11, 42], 88]))


def myFilter(f,L):
    '''takes in f and outputs true or false
    second function inputs a list L and outputs only true objects of L'''
    if L==[]:
        return []
    if f(L[0])==True: 
        return [L[0]]+ myFilter(f,L[1:])
    return []+myFilter (f,L[1:])
print(myFilter(lambda x: x % 2 == 1, [6, 5, 4, 3, 2, 1]))


def deepReverse(L):
    ''' input as list of elements returns the lst and the items inside reversed.'''
    if L==[]:
        return L
    if isinstance(L[0], list):
        return deepReverse(L[1:])+ [deepReverse(L[0])]
    return deepReverse(L[1:])+[L[0]]

print (deepReverse([1, [2, 3], 4]))