
import re
string="Simple is better than complex. Complex is better than complicated."
pattern=re.compile(r'is')
obj=pattern.match(string)
obj=pattern.search(string)
print (obj.start(), obj.end())

obj=pattern.findall(string)
print (obj)

obj=pattern.sub(r'was', string)
print (obj)