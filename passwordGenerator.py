import string
import random

password_combi=string.ascii_letters+string.digits+string.punctuation

len_of_pass=int(input("Enter the length of password: "))
password=''.join(random.choices(password_combi,k=len_of_pass))
print("Your password is ",password)

