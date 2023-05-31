import random
# Get number of characters
number = int(input("Enter Enter the number of characters: "))
old_password = input("Enter your old password: ")
# Useful characters in password 
character="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# Making password
password =  " ".join(random.sample(character, old_password, number ))
# Print password
print (password)
