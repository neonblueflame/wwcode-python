""" The Challenge
Author: Neonblueflame
Description: Aling Nena’s Sari-sari store 
wants a robot that will ask the customer 
their total bill and payment amount and tell 
them their change (for now, we can allow 
negative change). 

For example:
  How much is your total bill? 150
  How much is your payment? 200
  Hi! Your change is 50.00
"""

bill = int(input('How much is your total bill? '))
payment = int(input('How much is your payment? '))

print(f'Hi! Your change is {bill - payment}')  
