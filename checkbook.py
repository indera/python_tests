
from money import Money
import sys


def main():
    money = Money(0)

    while True:
        try:
            what = int(raw_input("\nWhat do you want to do today?"
                                 "\n 1. Go home \n"
                                 "\n 2. Deposit money \n"
                                 "\n 3. Extract money \n"
                                 "\n 4. Deposit bitcoins \n"
                                ))
            if what == 1:
                print("Yay...")
                sys.exit()
            if 2 == what:
                print("\n Current balance: ${} ".format(money.get_amount()))
                amount = float(raw_input("Please enter the amount to add: \n "))
                money.add(amount)
                print("\n New balance: ${} ".format(money.get_amount()))
            if 3 == what:
                print("Current balance: ${} ".format(money.get_amount()))
                amount = float(raw_input("Please enter the amount to extract: \n"))
                money.subtract(amount)
                print("New balance: ${} ".format(money.get_amount()))
            if 4 == what:
                print("\n Current balance: ${} ".format(money.get_amount()))
                amount = float(raw_input("Please enter the amount of bitCoinZ to deposit: \n"))
                bc = Money(amount)
                money.add(bc.convert_to_bit())
                print("\n New balance: ${} ".format(money.get_amount()))
        except Exception:
            print("Nope")

if __name__ == '__main__':
    main()
