import re

pattern = r"apple"

text = "I have an apple and a banana"

match = re.search(pattern, text)

if match:
    print("Pattern Has Been Found!")
else:
    print("Pattern not found")