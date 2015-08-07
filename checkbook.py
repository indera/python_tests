__author__ = "Roy Keyes"
__copyright__ = "Copyright 2014, University of Florida, Clinical Translational Science Institute Informatics & Technology"
__credits__ = [""]
__license__ = "BSD 3 Clause"
__version__ = "0.0.1"
__maintainer__ = "Roy Keyes"
__email__ = "keyes@ufl.edu"
__status__ = "Development"

from money import *
import sys
import time
from decimal import *

class Checkbook(object):

    def __init__(self, balance=0):
        self._money = Money(balance)

    def main(self):

        while True:
            try:
                action = int(raw_input('\n\t1) Check Balance'
                                       '\n\t2) Deposit USD'
                                       '\n\t3) Withdraw USD'
                                       '\n\t4) Exit'
                                       '\n'
                                       '\n\tWhat do you want to do today? '))

                if action == 1:
                    self.check_balance()
                elif action == 2:
                    amount_to_deposit = Decimal(raw_input('\tAmount? '))
                    self._money.add(amount_to_deposit)
                    self.check_balance()
                elif action == 3:
                    amount_to_withdraw = Decimal(raw_input('\tAmount? '))
                    current_amount = self._money.get_amount()
                    if current_amount > amount_to_withdraw:
                        self._money.subtract(amount_to_withdraw)
                        self.check_balance()
                    else:
                        print('\tYou do not have enough $ (' + str(current_amount) + ')')
                elif action == 4:
                    sys.exit()

            except ValueError:
                print('You must enter a valid option')

        sys.Exit()

    def check_balance(self):
        self.respond('Checking your balance', 'Your balance is: ' + str(self._money.get_amount()), 1)

    def respond(self, action, text, sleep_time):
        print(chr(27) + "[2J")
        print('\t' + str(action) + '...')
        time.sleep(sleep_time)
        print(chr(27) + "[2J")
        print('\t' + text + '\n')

if __name__ == '__main__':
    try:
        print(chr(27) + "[2J")
        checkbook = Checkbook()
        checkbook.main()
    except KeyboardInterrupt:
        print(chr(27) + "[2J")
        sys.exit()

