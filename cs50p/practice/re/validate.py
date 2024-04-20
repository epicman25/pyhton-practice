import re

email = input("Email : ").strip()

if re.search(".+@.+",email):
    print("Valid")
else:
    print("Invalid")