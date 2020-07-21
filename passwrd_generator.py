import string
import random

# password generator function

def generate_pass(passwrd_len):
    characters = string.ascii_letters + string.digits + string.punctuation
    character = list(characters)
    random.shuffle(character)
    strong_pass = character[:passwrd_len]
    return strong_pass

print("\n\n\n ____ PASSWORD GENERATOR ______ \n\n\n")
print(" >>> How many characters you want in your password? \n")
pass_len = int(input(" password length : "))   
passwrd = generate_pass(pass_len)
print("\n\n your STRONG password : " + "".join(passwrd))

