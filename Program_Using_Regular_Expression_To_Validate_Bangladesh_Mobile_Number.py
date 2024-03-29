import re

def validate_Bangladesh_Mobilenumber(phonenumber):
    pattern = r"\+(880)-?[6-9][0-9]{9}$"  # Allow numeric characters, and hyphens, with a length of 10 characters
    return bool(re.match(pattern, phonenumber))

phonenumber = "+880-9715299537"
if validate_Bangladesh_Mobilenumber(phonenumber):
    print("Valid Bangladesh Number")
else:
    print("InValid Bangladesh Number")