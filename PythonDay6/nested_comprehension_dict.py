
# given string
l="ABC"

# using dictionary comprehension
dic = {
    x: {y: x + y for y in l} for x in l
}

print(dic)
