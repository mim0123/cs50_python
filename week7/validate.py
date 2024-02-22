import re
email = input("what's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("valid")
else:
    print("Invalid")
