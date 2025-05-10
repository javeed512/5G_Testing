
#without  comprehension list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#with comprehension list
fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x  for x in fruits   if "a" in x]
print(newlist1)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in fruits]
print(newlist)