"""
Exercise 2:
Make a list that includes four careers, such as 'programmer', 'truck driver', etc....
Use the list.index() function to find the index of one career in your list.
Use the in function to show that this career is in your list.
Use the append() function to add a new career to your list.
Use the insert() function to add a new career at the beginning of the list.
Use a loop to show all the careers in your list.
"""

careers = [
    "programmer",
    "truck driver",
    "scientist",
    "maid"
]

print(careers.index("programmer"))
print("maid" in careers)

careers.append("librarian")
print(careers)

careers.insert(0, "gardener")
print(careers)

for career in careers:
    print(career)