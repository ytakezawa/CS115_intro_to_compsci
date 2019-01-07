'''
Created on Oct 27, 2017

I pledge that I have abided by the Stevens Honor System. ytakezaw

@author: Yoshika Takezawa
'''

'''HELPER FUNCTIONS'''
def inverse(S):
    '''inverts 0s to 1s and 1s to 0s'''
    if S=='':
        return ''
    if S[0]=='0':
        return '1'+inverse(S[1:])
    return '0'+inverse(S[1:])
def btn_pos(s):
    '''converts binary to integers'''
    if s == '':
        return 0
    if int(s[0])== 0:
        return btn_pos(s[1:])
    return 2**(len(s[1:])) + btn_pos(s[1:])
def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    def ih(s):
        x= str(int(s)+1)
        if len(x)<8:
            x='0'*(8-len(x))+x
        if s=='':
            return 0
        if x[-1]== '1':
            return x[:-1] + '1'
        return increment(x[:-1]) + '0'
    if len(ih(s))>8:
        return ih(s)[-8:]
    return ih(s)
def ntb(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n ==0: 
        return ''
    return ntb(n//2)+ str(n%2)



'''__________________ACTUAL FUNCTIONS______________________'''
def TcToNum(S):
    '''converts 8-bit string to the corresponding integer
    if the string begins with a 0, the function calls the helper
    if otherwise, invert numbers and add 1 to get positive number, 
    convert it, and mult it by -1 '''
        
    if S[0]=='0':
        return btn_pos(S)
    return btn_pos(increment(inverse(S)))*-1
#print(TcToNum('1000000'))


def NumToTc(N):
    '''takes in the integer and outputs the binary
    if negative, flip and add 1'''
    if N>=128 or N<-128:
        return 'Error'
    
    '''takes the absolute number of N and converts to binary'''
    result= ntb(abs(N))
    
    '''string length control'''
    if len(result)<8:
        result= '0'*(8-len(result))+result
    elif len(result)<8:
        result= result[-8:]
    
    '''if N is negative, it inverts the numbers and adds 1
    if otherwise, the result is output'''
    if N<0:
        return increment(inverse(result))
    return result
#print(NumToTc(-32))