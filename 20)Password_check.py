"""	check if Password is valid or not. Note: minimum 8 characters, 1 upper case characters, 1 special character, 
    should not begin with digit, check if password is valid or not."""

print('\nNote: minimum 8 characters, 1 upper case characters, 1 special character, should not begin with digit\n')
password = input("Enter your password: ")
if len(password) < 8:
    print("Password is too short")
elif password[0].isdigit():
    print("Password cannot start with a digit")
elif password.isalnum():
    print("Password should contain at least one special character")
elif password.islower():
    print("Password should contain at least one upper case character")
else:
    print("Password is valid")