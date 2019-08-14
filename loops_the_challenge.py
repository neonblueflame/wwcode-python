""" Aling Nena's Cashier Challenge
Author:
Description: During closing, Aling Nena counts from her vault the day's total income and
also the total amount of all her paper bills.

Help Aling Nena count her total income and total amount of her paper bills
from a list of cash money and using a loop!
"""


def is_coins(money):
    """ Determine if the money is a coin
    :param money: (Integer)
    :return: (Boolean)

    Examples:
        >>>  print(is_coins(20))
        False
        >>>  print(is_coins(1))
        True
    """
    if money < 20:
        return True
    return False


cash_on_vault = [1, 5, 100, 10, 50, 50, 20, 5, 1, 1000, 1000, 500, 5, 200]

# Build your code below

coins_total = 0
bills_total = 0

for cash in cash_on_vault:
  
    if is_coins(cash):
        coins_total = coins_total + cash
    else:
        bills_total = bills_total + cash
        
print(f"Hi Aling Nena! Your total income for the day is {coins_total + bills_total}.")
print(f"The total amount of your paper bills is {bills_total}.")