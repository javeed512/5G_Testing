
keys= [10,20,30,40,50]
values = ["orange", "mango", "kiwi", "pineapple", "banana"]

#comprehension dictionary below
fruitsDict = {k:v.upper()   for(k,v) in zip(keys,values)  if k > 20}

print(fruitsDict)