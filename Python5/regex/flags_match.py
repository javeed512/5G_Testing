

import re
line = "are smarter  Dogs than Cats";
matchObj = re.match( r'cats', line,re.I|re.M)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
searchObj = re.search( r'dogs', line)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")