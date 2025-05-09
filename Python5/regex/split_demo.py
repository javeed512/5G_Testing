
import re

text = "apple,banana;orange grape"
result = re.split(r"[,; ]", text)
print(result)  # Output: ['apple', 'banana', 'orange', 'grape']

text = "1+2*3-4/5"
result = re.split(r"[+\-*/]", text)
print(result) # Output: ['1', '2', '3', '4', '5']

text = "one two\tthree\nfour"
result = re.split(r"\s+", text)