
class EvenNumbers:
    def __iter__(self):
        self.n = 10  # Start from the first even number
        return self

    def __next__(self):
        x = self.n
        self.n += 4  # Increment by 2 to get the next even number
        return x

# Create an instance of EvenNumbers
even = EvenNumbers()
it = iter(even)


# Iterate until StopIteration is raised
i=1
while i < 5 :
    try:
        print(next(it))
        i = i+1
    except StopIteration:
        print("End of iteration")
        break


print(EvenNumbers.__doc__)
help(EvenNumbers)
