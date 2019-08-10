""" Aling Nena's Reward System Challenge
Author: 
This summer, Aling Nena’s Sari-sari store wants to 
implement a reward system where customers can redeem 
a reward by texting the following:
<Reward number 1-9> <Customer’s name> <Gender f or m>

>> Please enter text: 1 nicole i. tibay f

The system will then reply the following:
Hi <Customer’s name Capitalized>! You have successfully 
redeem reward #<reward number> - <reward>! Thank you for 
choosing Aling Nena’s Sari-sari store.

Let’s assume that customers will always comply with the 
text format and give 1-9 number.

>> Hi Nicole I. Tibay! You have successfully redeem reward #1 - Coke sakto!
Thank you for choosing Aling Nena’s Sari-sari store.
"""

# You can access this by: rewards[<index>]
# Just like strings the index starts with 0
rewards = [
    "Coke sakto",  # index 0
    "Boy Bawang",  # index 1
    "15pcs. Yucky candy",  # index 2
    "15pcs. Pintura candy",  # index 3
    "15PHP load",  # index 4
    "3 pcs. Dove conditioner",  # index 5
    "Cottonbuds",  # index 6
    "One sheet of Biogesic",  # index 7
    "100mL Pepper/Pintura",  # index 8
]

text = input("Please enter text: ")

choice = text[0]

name_raw = text[2:-2]
name_arr = name_raw.split(" ")

i = 0
for word in name_arr:
  name_arr[i] = word[0].upper() + word[1:len(word)]
  i += 1
  
name = " ".join(name_arr)
  
print(f"Hi {name}! You have successfully redeem reward #{choice} - {rewards[int(choice)]}! Thank you for choosing Aling Nena’s Sari-sari store.")