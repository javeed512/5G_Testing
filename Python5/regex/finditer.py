

import re
string="Simple is better than complex. Complex is better than complicated."
pattern=re.compile(r'is')
iterator = pattern.finditer(string)
#print (iterator )

for match in iterator:
   print(match.span())