
from functools import reduce

# Example: Find the product of all numbers in a list
a = [1000, 2000, 3000, 4000]
b = reduce(lambda x, y: x + y, a)  # sum of nums
print(b)