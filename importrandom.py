import random

print("randopassword App")
print("Hello! let's create a password for you")


### Define list of random characters
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+" 


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
    
    
while True:
    user_input = input ("Do you want to generate another password? (y/n): ")
    
### Checks if user wants to generate another password, creates new Generation
    if user_input in ["y", "yes"]:
        print("\n")
        print("Let's generate a new password!")
        passwordLength = int(input("Enter the length of the password: "))
        newPassword = []
        for x in range(passwordLength):
            newPassword.append(random.choice(characters))
        finalPassword = ''.join(map(str, newPassword))
        print("\n this is your new password: ", finalPassword)

    elif user_input in ["n", "no"]:
        print("Goodbye!")
        break

    else:
        print ("\n")
        print("Invalid input. Please type 'y' or 'n'")
        
