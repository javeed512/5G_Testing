
import argparse

parser = argparse.ArgumentParser(description= 'finding argument details in current file')

 #sys.argv
parser.add_argument("name")
parser.add_argument("age")

args =   parser.parse_args()

print(args)

print(args.name)
print(args.age)


if args.name=="Admin":
   print ("Hello Admin")
else:
   print ("Hello Guest")