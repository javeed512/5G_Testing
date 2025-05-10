

def add(a,b):
    return a+b   

f1  =    lambda  a,b:  a+b; 

print(f1.__doc__)
help(f1)

print("lambda func called ",f1(4,5))


# Example: Check if a number is positive, negative, or zero
validate = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(validate(0))   

