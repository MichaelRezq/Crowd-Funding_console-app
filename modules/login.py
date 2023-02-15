import userDataHandling
import re


# list of the users that are already signed up
listOfUsers = userDataHandling.read_jaon(
    "./Crowd-Funding_console-app/json/usersData.json")
# print(listOfUsers)

# login form
regex = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

# handling email


def emailLogin():
    while True:
        mail = input('Type your email: ')
        if re.fullmatch(regex, mail):
            # check if the mail is exist to log in
            for user in listOfUsers:
                # print(user["email"])
                if user["email"] == mail:
                    userpassword = user["password"]
                    # check if the password is right
                    passwordLogin(userpassword)
                    userMail = {"useremail": mail}
                    # append the  user mail to online users json file
                    userDataHandling.write_json(
                        userMail, "./Crowd-Funding_console-app/json/onlineUsers.json")
                else:
                    print("looks like you didnot sign up yet , signup first")
                    break
                break
        else:
            print('Type a valid email')
            continue
        break

# password handling


def passwordLogin(userpassword):
    while True:
        password = input('Type your password: ')
        if password:
            if password == userpassword:
                print('you loged in successfully')
            break
        else:
            print('Type your email password')
            continue
