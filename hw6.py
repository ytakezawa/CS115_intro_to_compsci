'''
Created on Oct 13, 2017

I pledge that I have abided by the Stevens Honor System. ytakezaw

@author: Yoshika Takezawa
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.



# THE DOCUMENT QUESTIONS
# explain what is the largest number of bits that your compress algorithm could
# possibly use to encode a 64-bit string/image
# --- it is 5* 64 because if it is 1010101010..., the program would say '00001' 64 times. 
# 
# describe the tests that you conducted and the compression ratios that you found. 
# --- "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"
#           outputs 1.015625
# "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
#           outputs 1.328125
#"00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
#           outputs 1.484375
#the compressed size is larger than the original. 
# 
# the algorithm cannot exist. why?
# --- because compressing the data more would skew the results themselves...?

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n ==0: 
        return '00000'
    result= numToBinary(n//2)+ str(n%2)
    if len(result) < COMPRESSED_BLOCK_SIZE:
        return '0'*(COMPRESSED_BLOCK_SIZE-len(result)) + result
    return result[-COMPRESSED_BLOCK_SIZE:]
#print(numToBinary(0))

def binaryToNum(s):
    '''GOES RIGHT TO LEFT!!!! Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def binaryToNum_h(s,x, accum):
        if s == '':
            return accum
        if int(s[-1])==0:
            return binaryToNum_h(s[:-1], x+1, accum)
        return (2**x)+(binaryToNum_h(s[:-1], x+1, accum))
    return binaryToNum_h(s,0,0)
#print(binaryToNum('101010'))

def countRun(s, c, maxRun):
    '''parameter s is a string
    c is what were counting
    maxRun- maximum length of run
    takes a string returns the number of times 
    that string occurs in a row.'''
    if s =='' or c== '':
        return 0
    if s[0]!=c:
        return 0  
    x= 1+countRun(s[1:], c, maxRun)
    if x>maxRun:
        return maxRun
    return x
#print(countRun('0'*32, '0', MAX_RUN_LENGTH))


def compress(s):
    '''return compressed string
    count the runs in s switching from counting runs of zeros to counting runs of ones'''
    def compress_help(s,c):
        if s == '':
            return ''
        runLen = countRun(s, c, MAX_RUN_LENGTH)
        nextC = '0'
        if c =='0':
            nextC = '1'
        return numToBinary(runLen)+ compress_help(s[runLen:], nextC)
    return compress_help(s, '0')


def uncompress(s):
    ''' param s --
    in chucks of COMPRESSED_BLOCK_SIZE, 
    convert the binary representation of a number 
    in that block into that many zeros or ones, switching
    from decompressing zeros to decompressing ones alternatively
    return decompressed string'''
    def uncompress_help(s, c):
        if s =='':
            return ''
        first5 = s[:COMPRESSED_BLOCK_SIZE]
        x = binaryToNum(first5)
        nextC = '0'
        if c =='0':
            nextC = '1'
        return x*c + uncompress_help(s[COMPRESSED_BLOCK_SIZE:], nextC)
    return uncompress_help(s, '0')
#print(compress('1111100000111110000000010'))
#print(uncompress('00000001010010100101010000000100001'))

def compression(s):
    ''' return divide compressed size by original size--length'''
    return len(compress(s))/len(s)

#print(compress('0010'*16))
#print(compression('0010'*16))


