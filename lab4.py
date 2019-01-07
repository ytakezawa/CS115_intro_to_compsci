'''
Created on Sep 28, 2017

I pledge that I have abided by the Stevens Honor System.  ytakezaw

@author: Yoshika Takezawa
'''

def knapsack(capacity, itemList):
    '''returns the maximum value and the list of items that make that value,
     without exceeding the capacity
     '''
    if capacity == 0 or itemList ==[]:
        return [0,[]]
    if itemList[0][0]>capacity:
        return knapsack(capacity, itemList[1:])
    use_it = knapsack(capacity-itemList[0][0], itemList[1:])
    value = itemList[0][1] + use_it[0]
    lose_it = knapsack(capacity, itemList[1:])
    if value > lose_it[0]:
        return [value, [itemList[0]] + use_it[1]]
    return lose_it


