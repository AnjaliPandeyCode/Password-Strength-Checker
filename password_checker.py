# password strength checker

import re               # importing re module which helps to search special character

# password strength check conditions:
# min 8 chars, digit, uppercase, lowercase, special characters

def check_password_strength(password):
    if len(password) < 8:  # checking length of password
        return "Weak: Password must be atleast 8 characters"
    
    if not any(char.isdigit() for char in password): # char.isdigit() is a method that tells whether the charcters are numerical value or not 
        return "Weak: Password must contain a digit"
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain an upper letter"
    
    if not any(char.islower() for char in password):
        return "Weak: Password must contain a lower letter"
    
    if not re.search(r'[!@#$%^&*(){}<>.?]', password):
        return "Medium: Password must contain a special characters"
    
    return " Strong: Your password is secured!"

def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Thank you for using this tool")
            break

        result = check_password_strength(password)
        print(result)

# Run the password checker tool
if __name__ == "__main__": # it's like a main gate, you will choose which function to run inside and in which order
    password_checker()     