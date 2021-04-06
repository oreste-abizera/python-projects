import random

print("\nWelcome to Password generator\n")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-,.?<>:|0123456789'

num = input("How many passwords to generate: ")
num = int(num)

length = input("How many characters consisting the password: ")
length = int(length)

print("\nList of generated passwords:\n")

for pwd in range(num):
    password = ''
    for c in range(length):
        password += random.choice(chars)

    print(str(pwd+1) + ". " + password)
