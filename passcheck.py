import string
import re

def upperHere(string):
    return re.search(r"[A-Z]",string) is not None

def lowerHere(string):
    return re.search(r"[a-z]",string) is not None

def numberIsHere(string):
    return any(char.isdigit() for char in string)

def specialChars(string, punctuation=string.punctuation):
    return any(char in punctuation for char in string)

print("******************")
print("Password checker")
print("******************")

criteria = {
    "lengthMatch" : False,
    "HasUpCase" : False,
    "HasLowCase" : False,
    "NumHere" : False,
    "SpecialChars" : False,
}

while not all (criteria.values()):
    password = input("Enter you Password: ")

    if len(password) >= 8:
        criteria["lengthMatch"] = True
    else:
        print("password must be 8 characters or longer")

    if upperHere(password):
        criteria["HasUpCase"] = True
    else:
        print("The password should contain atleast one uppercasecharacter")

    if lowerHere(password):
        criteria["HasLowCase"] = True
    else:
        print("The password should contain atleast one lowercase character")

    if numberIsHere(password):
        criteria["NumHere"] = True
    else:
        print("The password should contain atleast one number")

    if specialChars(password):
        criteria["SpecialChars"] = True
    else:
        print("The password should contain atleast one special character")

print("Your password is Strong")