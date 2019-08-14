""" Challenge
Author:
Description: Aling Nena stores her soft drink stock on two refrigerators.
She stores Coke, Sprite and Royal on her Sari-sari store's refrigerator while
RC and 7UP can be found on her house's refrigerator.

Help Aling Nena to properly respond to her customer
when buying softdrinks.

The reply will depend if the soft drink brand is on the store's ref,
on the house's ref or none. If the customer buys a soft drink brand that is:
    1. stored on the store, she will respond 'Got it!'
    2. stored on the house, she will respond 'Please wait for a while!'
    3. not sold by her, she will respond 'Sorry we do not sell that. We only
    have <input here the soft drink brands>'
"""

ref_house = ["rc", "7up"]
ref_store = ["coke", "sprite", "royal"]

customer_order = input("Hi! What soft drink brand do you want? ")

if customer_order.lower() in ref_store:
    print("Got it!")
    
elif customer_order.lower() in ref_house:
    print("Please wait for a while!")

else:
    print("Sorry we do not sell that. We only have "
          + ", ".join(ref_house).upper()
          + ", "
          + ", ".join(ref_store).title()
          + ".")