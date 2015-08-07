#!/usr/bin/env python

from money import Money


#set the starting balance of the account
mynewlocalmoneyobject = Money(100)

#credit the checking balance with some amount
mynewlocalmoneyobject.add(100)

#debit the checking balance with some amount
mynewlocalmoneyobject.subtract(50)

#return the new balance
print mynewlocalmoneyobject.get_amount() 
