
str = 'Hello-Friends'

tuple = str.partition('-')

print("partiion ", tuple)



res = str.replace('Hello','Hi') 

print("replace ",res)


ind = str.find("Friends")

print("find index of Friends ",ind)

str2 = "*Wipro*" 

print(str2.strip('*') + "hello") 


str3 = "hi how are you"

print(str3.split())

str4 = "Tom is a good student"

print(str4.startswith("good",9))

str5 = '50000'

print(str5.isnumeric())

num = int(str5)

print(num)