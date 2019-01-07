'''
Created on Nov 20, 2017

I pledge my honor that I have abided by the Stevens Honor System. ytakezaw

@author: Yoshika Takezawa
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    
    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day
    
    def tomorrow(self):
        '''should not return anything, just adds one calendar day
        to the current day'''
        numDays = DAYS_IN_MONTH[self.month]
        if self.month == 12 and self.day ==31:
            self.year += 1
            self.month = 1
            self.day = 1
        elif self.month ==2 and self.day==numDays and self.isLeapYear():
            self.day+=1
        elif self.day >= numDays :
            self.month += 1
            self.day = 1
        else: 
            self.day +=1
    def yesterday(self):
        '''should not return anything, just subtracts one calendar day
        from the current day'''
        if self.month ==1 and self.day == 1:
            self.year -= 1
            self.month = 12
            self.day = DAYS_IN_MONTH[self.month]
        elif self.month == 3 and self.day == 1 and self.isLeapYear():
            self.month -=1
            self.day =29;
        elif self.day ==1:
            self.month -= 1
            self.day =DAYS_IN_MONTH[self.month]
        else: 
            self.day -=1
    
    def addNDays(self, N):
        '''prints all the dates between the start date and the end date, 
        changes the date N calendar days from the start date'''
        for _ in range(N):
            print(self)
            self.tomorrow()
        print(self)

    def subNDays(self, N):
        '''much like addNDays, but subtracts days'''
        for _ in range(N):
            print(self)
            self.yesterday()
        print(self)
    
    def isBefore(self, d2):
        '''returns True if the calling object is a calendar date before d2
        If self and d2 represent the same day,this method should return False. 
        Similarly, if self is after d2, this should return False.'''
        if self.year < d2.year:
            return True
        elif self.year ==d2.year and self.month < d2.month:
            return True
        elif self.year ==d2.year and self.month == d2.month and self.day < d2.day:
            return True
        else: 
            return False
    
    def isAfter(self, d2):
        '''returns True if the calling object is a calendar date after d2
        If self and d2 represent the same day,this method should return False. 
        Similarly, if self is before d2, this should return False.'''
        if self.isBefore(d2) or self.equals(d2):
            return False
        return True
    
    def diff(self, d2):
        '''returns an integer representing the number of days between self and d2.'''
        date1=self.copy()
        date2=d2.copy()
        count = 0
        if date1.isAfter(date2)==True:
            while date1.isAfter(date2):
                date1.yesterday()
                count +=1
        elif date1.isBefore(date2)==True:
            while date1.isBefore(date2):
                date1.tomorrow()
                count -=1
        return count
    
    def dow(self):
        ''' returns the day of the week'''
        listOfDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        knownDow = Date(11, 26, 2017) #is a Sunday
        difference = knownDow.diff(self)
        return listOfDays[(-difference)%7]