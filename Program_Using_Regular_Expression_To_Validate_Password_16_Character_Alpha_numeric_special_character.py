import re

def validate_phone_number(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{16}$'  # Allow alphanumeric characters, spaces, and hyphens, with a length of 16 characters
    return bool(re.match(pattern, password))

password = "alsf#%ASDE@x@4td"
if validate_phone_number(password):
    print("Valid Password")
else:
    print("Invalid Password")