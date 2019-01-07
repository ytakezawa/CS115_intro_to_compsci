'''
Created on Oct 12, 2017

I pledge my honor that I have abided by the Stevens Honor System. ytakezaw

@author: Yoshika Takezawa
'''


def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n%2 ==1:
        return True
    return False

'''
DOCUMENT QUESTIONS
42 base 2:
largest power of 2 that goes into 42 is 32(2^5)   42-32=10   1
next power of 2 is 16(2^4) but 16 doesn't go into 10.        0
largest power of 2 that goes into 10 is 8(2^3)    10-8=2     1
next power of 2 is 4 (2^2), but 4doesn't go into 2.          0
largest power of 2 that goes into 2 is 2(2^1)     2-2=0      1
next power of 2 is 1 (2^0), 1 but doesn't go into 0.         0  (read the numbers top to bottom)

 If you are given an odd base-10 number, what will the least-significant bit - the
rightmost bit - be in its base-2 representation? Similarly, if you are given an even base-10
number, what will the least-significant bit - the rightmost bit - be in its base-2 representation?
--------The right most bit will be 1 if the number is odd; The right most bit will be 0 if the number is even

If we remove the least significant bit(the right most bit), 
what is happening to the original number?
--------By removing the least significant bit, we are dividing the number in half and rounding up 

 If we already had the base-2
representation of Y, perhaps from recursion, how would this allow us to easily find the base-2
representation of N? (You'll need two answers here: one in the case that N is odd and one in the
case that N is even.)
--------Let's say that N is even, then we can double Y(or add Y + Y) and get N
Let's say that N is odd, then we can double Y and subtract 2 and get N

'''

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n ==0: 
        return ''
    return numToBinary(n//2)+ str(n%2)
#print(numToBinary(100))

def binaryToNumNOPENOPE(s):
    '''NOT THIS ONE!! THIS GOES LEFT TO RIGHT'''
    if s == '':
        return 0
    if int(s[0])== 0:
        return binaryToNumNOPENOPE(s[1:])
    return 2**(len(s[1:])) + binaryToNumNOPENOPE(s[1:])
#print(binaryToNum1('101010'))

def binaryToNum(s):
    '''GOES RIGHT TO LEFT!!!! Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def binaryToNum_h(s,food, tada):
        if s == '':
            return tada
        if int(s[-1])==0:
            return binaryToNum_h(s[:-1], food+1, tada)
        return (2**food)+(binaryToNum_h(s[:-1], food+1, tada))
    return binaryToNum_h(s,0,0)
#print(binaryToNum('101010'))

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    def ih(s):
        xylophone= str(int(s)+1)
        if len(xylophone)<8:
            xylophone='0'*(8-len(xylophone))+xylophone
        if s=='':
            return 0
        if xylophone[-1]== '1':
            return xylophone[:-1] + '1'
        return increment(xylophone[:-1]) + '0'
    if len(ih(s))>8:
        return ih(s)[-8:]
    return ih(s)
#print(increment('11111111'))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    def count_h(s,n, accum):
        if s=='':
            return 0
        if n == 0:
            print(s)
            return accum
        print(s)
        return count_h(increment(s), n-1, accum)
    return count_h(s, n, '')
#print(count('00000000', 0))

'''
the tertnary number for 59 is 2011
59/3  is 19 remainder 1
19/3  is 6  remainder 1
6/3   is 2  remainder 0
2/3   is 0  remainder 2
'''


def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n ==0: 
        return ''
    return numToTernary(n//3)+ str(n%3)
#print(numToTernary(4242))

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    def ternaryToNum_h(s,food, tada):
        if s == '':
            return tada
        if int(s[-1])==0:
            return ternaryToNum_h(s[:-1], food+1, tada)
        if int(s[-1])==1:
            return (3**food)+(ternaryToNum_h(s[:-1], food+1, tada))
        return 2*(3**food)+(ternaryToNum_h(s[:-1], food+1, tada))
    return ternaryToNum_h(s,0,0)
#print(ternaryToNum('12211010'))
