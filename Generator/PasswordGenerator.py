import secrets # Used secrets library instead of the random library for security
import string 

# Custom exception for invalid input
class WrongInput(Exception):
    pass

# Start of the random password generator function :-

def PasswordGenerator(PasswordLength):
    
    Password = ""
    # All letters in the ASCII
    letters = string.ascii_letters
    # All digits in the ASCII
    digits = string.digits
    # All special_chars in the ASCII
    special_chars = string.punctuation
    # All of the above combined in the ASCII
    AllPossible = letters + digits + special_chars
    
    try:
        # Construction of the Password using secrets library and combined ASCII characters above :-
        for i in range(int(PasswordLength)):
            Password += ''.join(secrets.choice(AllPossible))
            
    except:
        # Raised custom exception in case of a nvalid input
        raise WrongInput
        
    return Password


# command to run the program on the server

# cd /Users/devansh/Desktop/Password-Generator && python3 server.py

# cd "location of the directory" && python3 "name of the server file"


