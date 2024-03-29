import re

def validate_US_Phonenumber(phonenumber):
    pattern =  r"\+(1)-\d{3}-\d{3}-\d{4}"  # Allow numeric characters, and hyphens, with a length of 3,3,4 characters
    return bool(re.match(pattern, phonenumber))

phonenumber = "+1-555-555-0007"
if validate_US_Phonenumber(phonenumber):
    print("Valid USA Number")
else:
    print("Invalid USA Number")