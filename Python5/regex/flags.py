
import re

text = "first line\nsecond line\nthird line"

# Without re.M
print(re.findall(r"^\w+", text))
# Output: ['first']

# With re.M
print(re.findall(r"^\w+", text, re.M))
# Output: ['first', 'second', 'third']
