import string
import random

chars=string.ascii_letters + string.digits + string.punctuation
c=""
n=int(input("Enter the length of password: "))
for i in range(n):
    c+=random.choice(chars)
print(f"Generated password: {c}")
