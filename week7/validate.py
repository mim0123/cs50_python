import re
email = input("what's your email? ").strip()

if re.search(".+@.+", email):
    print("valid")
else:
    print("Invalid")

