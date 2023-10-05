import re

text = "My phone number is 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"

match = re.search(pattern,text)
if match:
    phonenumber = match.group()
    print("Phone number Found:" , phonenumber)
else:
    print("Phone Number not found!")