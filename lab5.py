'''
Created on Oct 5, 2017

I pledge my honor that I have abided by the Stevens Honor System

@author: Yoshika Takezawa
'''
import time
from cs115 import map

words = []
HITS = 10


def fastED(S1,S2):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def fastED_h(S1, S2, memo):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        if S1 == '':
            result = len(S2)
        elif S2 == '':
            result = len(S1)
        elif S1[0] == S2[0]:
            result= fastED_h(S1[1:], S2[1:], memo)
        else:
            substitution = 1 + fastED_h(S1[1:], S2[1:], memo)
            deletion = 1 + fastED_h(S1[1:], S2, memo)
            insertion = 1 + fastED_h(S1, S2[1:], memo)
            result= min(substitution, deletion, insertion) 
        memo[(S1, S2)] =result
        return result
    return fastED_h(S1, S2, {})
#print(fastED("antidisestablishment", "antiquities"))


def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda n: [fastED(user_input, n), n], words)


def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()

