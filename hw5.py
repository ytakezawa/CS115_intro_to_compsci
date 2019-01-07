'''
Created on Oct 8, 2017

I pledge that I have abided by the Stevens Honor System. ytakezaw

@author: Yoshika Takezawa
'''

import turtle

def sv_tree(trunk_length, levels):
    '''create a sideways tree using turtle'''
    if levels == 0:
        return 
    turtle.forward(trunk_length)
    turtle.left(22.5)
    sv_tree(trunk_length/2, levels-1)
    turtle.right(45)
    sv_tree(trunk_length/2, levels-1)
    turtle.left(22.5)
    turtle.backward(trunk_length)
    
#print(sv_tree(100, 4))

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def flh(n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            result = 2
        elif n == 1:
            result = 1
        else:
            result = flh(n-1, memo) + flh(n-2, memo)
        memo[n] = result
        return result
    return flh(n, {})
#print(fast_lucas(5))


def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, cointup, memo):
        if (amount, cointup) in memo:
            return memo[(amount, cointup)]
        if amount == 0:
            result = 0
        elif cointup == () or amount < 0:
            result = float("inf")
        else:
            huh1= fast_change_helper(amount - cointup[0], cointup, memo)+1
            huh2 = fast_change_helper(amount, cointup[1:], memo)
            result = min(huh1, huh2)
        memo[(amount, cointup)] = result
        return result
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})



# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
