import string
import random
length = int(input("Enter the desired length of the password: "))
def password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    return password
password = password(length)
print("Your generated password is: ", password)