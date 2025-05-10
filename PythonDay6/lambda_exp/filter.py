
# Example: Filter even numbers from a list
list1 = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, list1)
print(list(even))


list2 = [x  for x in range(100)]

f1  =  filter(lambda  i: i > 90 , list2)

print(list(f1))