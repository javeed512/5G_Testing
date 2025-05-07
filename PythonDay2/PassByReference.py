
def   myFunc(myList):

    print("myList before inside ",myList)

    myList.append(4)
    myList.extend([5,6])

    print("after modify myList inside ",myList)

list1 = [1,2,3]

print("list1  before passing ",list1)

myFunc(list1)

print("list1 after func call outside ",list1)

