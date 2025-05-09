
import re

pattern = '^p....n$'



txt1 = 'python'

isFound =   re.match(pattern,txt1)

if isFound:
    print('pattern found successfully in text')
else:
    print('pattern not found , failed')

