
newlist = [x for x in range(10) if x < 5]

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper()  for x in fruits]

print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ["Mr."+x    for x in fruits]

print(newlist)

# Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits ]

print(newlist)

fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']

print(newlist)

newlist = [len(x)  for x in fruits]
print(newlist)