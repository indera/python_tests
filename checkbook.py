#!/usr/bin/env python

from money import Money


#set the starting balance of the account
mynewlocalmoneyobject = Money(100)


#credit the checking balance with some amount
mynewlocalmoneyobject.add(100)

#debit the checking balance with some amount
mynewlocalmoneyobject.subtract(50)

#return the new balance
print "Your starting balance was 100. You deposited 100. You withdrew 50. Your new balance is: $",mynewlocalmoneyobject.get_amount() 
