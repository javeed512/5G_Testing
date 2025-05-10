
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thatlist= [10,20,30,40,50]
thislist.sort()
print(thislist)

mylist = thislist.copy()
print(mylist)


#finallist = thislist + thatlist
finallist =  thislist.extend(thatlist)

print(thislist)



