from random import randrange

is_hungry = True
foods = ["apple", "biscuit", "bread", "carrot", "blueberry"]

while is_hungry:
    is_hungry = input("Are you hungry? ")
    if is_hungry.lower() == "no":
        break
    else:
      print(f"Then eat {foods[randrange(5)]}.")
    
    print("Something")