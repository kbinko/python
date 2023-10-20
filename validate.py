import re

email = input("Enter your email: ").strip()

if re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email, re.IGNORECASE):
    print("Valid email")
else:
    print("Invalid email")