import random

print("randpassword")
print("Hello! let's createa a password for you")


### Define list of random characters
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+" 
numbers = "1234567890"


### Get the length of the password 
passwordLength = int(input("Enter the length of the password: "))


### generate the password
newPassword = []
for x in range(passwordLength):
    ###Append a random chracter to the password string
    newPassword.append(random.choice(characters))


###join whole list back into a string
finalPassword = ''.join(map(str, newPassword))


### Print new password
print("\n this is your new password: ", finalPassword)
    
