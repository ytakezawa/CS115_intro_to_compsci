'''
Created on Nov 16, 2017

I pledge my honor that I have abided by the Stevens Honor System. ytakezaw

@author: Yoshika Takezawa
'''
import math

class QuadraticEquation(object):
    '''finds the roots of a quadratic function'''
    def __init__(self, a, b, c):
        '''initializes the variables'''
        a= float(a)
        b= float(b)
        c= float(c)
        
        self.__a= a
        '''raises error if a=0 the function is linear'''
        if self.__a ==0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.__b= b
        self.__c= c
    @property
    def a(self):
        return self.__a
    @property
    def b(self):
        return self.__b
    @property 
    def c(self):
        return self.__c
    
    
    def discriminant(self):
        '''computes b^2 -4ac'''
        a = self.__a
        b = self.__b
        c = self.__c
        return (b **2) -(4 * a * c)
    

    
    def root1(self):
        '''computes(-b + sqrt(discriminant))/(2a'''
        a = self.__a
        b = self.__b
        c = self.__c
        d = self.discriminant()
        if d <0:
            return None
        return (-b + (math.sqrt(d)))/(2*a)
    
    def root2(self):
        '''computes(-b - sqrt(discriminant))/2a'''
        a = self.__a
        b = self.__b
        c = self.__c
        d = self.discriminant()
        if d <0:
            return None
        return (-b - (math.sqrt(d)))/(2*a)
    
    def __str__(self):
        '''displays equation as ax^2 + bx + c = 0
        If a is negative, put a minus sign in front.
o If b or c is negative, the plus sign should be converted into a minus sign.
o If b is 0, do not display that term.
o If c is 0, do not display that term.
o If a or b is 1, do not display it.'''
        a = self.__a
        b = self.__b
        c = self.__c
        
        if a<0:
            a = '-x^2' 
        elif a == 1:
            a = 'x^2'
        else:
            a = '%sx^2' % a
         
         
        if b == 0:
            b = ''
        elif b ==1:
            b = ' + x'
        elif b == -1:
            b= ' - x'
        elif b < 0:
            b = ' - %sx' % (b * -1)
        else:
            b = ' + %sx' % b
        
        
        if c < 0:
            c= ' - %s' % (c * -1)
        elif c==0:
            c= ''
        elif c > 0:
            c= ' + %s' % c
        
        return a + b + c + ' = 0'
    
