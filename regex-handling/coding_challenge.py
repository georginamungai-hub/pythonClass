import re

phonePattern = r"\d{3}[-.\s]\d{3}[-.\s]\d{4}[-.\s]"

emailPattern = r"^[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                
string = "Please contact info@example.com for assistance. Phone:123 456-7890 or 111 222-3333 "


def extract_phone_numbers(string):
    match = re.search(phonePattern, string)
    if match:
        phoneNumbers = match.group()
        return phoneNumbers
    else:
        return 'No Phone Number Found'
    

def extract_email_addresses():
    match = re.search(emailPattern, string)
    emails = match.group()
    return emails

def replace_email_addresses(string, replacement):
    replace = re.sub(emailPattern, replacement, string)
    return replace

# string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"
print(extract_phone_numbers(string))
print(extract_email_addresses())
print(replace_email_addresses(string, "REPLACED"))