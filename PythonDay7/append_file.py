
file = open("hello.txt","at+")

file.write('This is python')

file.seek(0) # move cursor pointer to the begining of the file

data = file.read(13)

print(data)