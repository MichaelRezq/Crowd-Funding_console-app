
# the user date and save each user data in a dictionary , and append that dictionary in a list
import json
import re
import time
import userDataHandling
personalData = {}

# list of the users that are already signed up
listOfUsers = userDataHandling.read_jaon(
    "./Crowd-Funding_console-app/json/usersData.json")
# generate Id using time


def generateIdUsingTime():
    personalData["id"] = round(time.time())

# validate name


def validateName(level):
    while True:
        name = input(f'type your {level} name: ')
        if name.isalpha() == True:
            personalData[f"{level}Name"] = name
            break
        else:
            print('type valid name')

# validate age


def validateAge():
    while True:
        age = input('type your age: ')
        if age.isdigit() == True:
            personalData["age"] = age
            break
        else:
            print('type a valid age')

# validate gender


def validateGender():
    while True:
        gender = input('type your gender: ')
        if gender.lower() == 'male' or gender.lower() == 'female':
            personalData["gender"] = gender
            break
        else:
            print('type valid gender')


# validate the email
regex = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"


def validateemail():
    while True:
        mail = input('Type your email: ')
        if re.fullmatch(regex, mail):
            # check if the mail is exist to log in
            for user in listOfUsers:
                # print(user["email"])
                if user["email"] == mail:
                    print("looks like you have sign up before , login now")
                    break
                else:
                    personalData["email"] = mail
                    break
        else:
            print('Type a valid email')
            continue
        break

# validate phone


phoneReg = "^01[0125][0-9]{8}$"


def validatePhone():
    while True:
        phone = input('Type your phone: ')
        if re.fullmatch(phoneReg, phone):
            personalData["phone"] = phone
            break
        else:
            print('Type a valid phone')
            continue

# validate password


def validatePassword():
    while True:
        password = input('Type your password: ')
        if len(password) > 0:
            personalData["password"] = password
            validateConfirmPassword(password)
            break
        else:
            print('your password cant be empty')
            continue

# confirmPassword


def validateConfirmPassword(password):
    while True:
        confirmPassword = input('Re-type your password: ')
        if confirmPassword == password:
            print('your password matches')
            break
        else:
            print('you did not match your password')
            continue

# after regesteration


def afterRegest():
    print("You have registered successfully")
# get personal data function


def getPersonalData():
    generateIdUsingTime()
    validateName("first")
    validateName("last")
    validateAge()
    validateGender()
    validateemail()
    validatePhone()
    validatePassword()
    userDataHandling.append_json(
        personalData, "./Crowd-Funding_console-app/json/usersData.json")
