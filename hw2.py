'''
Created on Sep 16, 2017

I pledge my honor that I abided by the Stevens Honor System. ytakezaw

@author: Yoshika Takezawa
'''

import sys
from cs115 import map, reduce, filter

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
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

'''remove,   is_word_possible,    list_of_words_created,    scoreList,    bestWord'''


def remove(letter, lst):
    '''removes a letter from a set of letters when used'''
    if lst == []:
        return []
    if letter == lst[0]:
        return lst[1:]
    return [lst[0]] + remove(letter, lst[1:])
#print(remove('a', ['b', 'b', 'c']))

def is_word_possible(S, lst):
    '''checks if the string is possible from the list of letters'''
    if S == '':
        return True
    if S[0] in lst:
        return is_word_possible(S[1:], remove(S[0], lst))
    return False
#print(is_word_possible('adasd', ['a','p','p','l', 'e']))

def list_of_words_created(Dictionary, letters):
    ''' creates a  list of possible words'''
    return filter(lambda word: is_word_possible(word,letters),Dictionary)
#print(list_of_words_created(Dictionary, ['a', 's','p','m', 't']))

def scoreList(Rack):
    '''takes in a list of lowercase letters and 
    outputs a list of possible words from the Dictionary and the scores'''
    
    letters= list_of_words_created(Dictionary, Rack)
    return map(lambda word: [word, wordScore(word, scrabbleScores)],letters)
#print(scoreList(['g', 'y','p']))

def bestWord(Rack):
    '''uses scoreList and only outputs the word with the highest score.
    if theres a tie, do whatever to choose just one.'''
    if list_of_words_created(Dictionary,Rack) == []:
        return ['', 0]
    contenders= scoreList(Rack)
    return reduce(lambda x, y: x if x[1]>y[1] else y, contenders)

#print(bestWord(['g', 'y','p']))