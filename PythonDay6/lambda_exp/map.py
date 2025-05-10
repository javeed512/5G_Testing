
# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))

list1 = ["king","smith","tom","javeed"]

findLen =    map(lambda s: len(s) , list1 )
print("length of each name")
print(list(findLen))


myfilter =  filter(lambda s: len(s) > 4 , list1) 

print(list(myfilter))