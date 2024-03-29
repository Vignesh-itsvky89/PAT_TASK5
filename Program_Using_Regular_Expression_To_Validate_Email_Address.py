import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
email_address = "1236hf@gmailcom.jg"
if validate_email(email_address):
    print("Email is valid.")
else:
    print("Email is invalid.")