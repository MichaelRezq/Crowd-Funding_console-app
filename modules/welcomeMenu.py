import signUp
import login
# first show menu to the user to login or sign up


def showMenu():
    print(" \n     **        welcome to our company      **      \n")
    while True:
        print("[1] to signup \n[2]to login\n")
        choice = input('\n===> Type ur choice: ')
        if choice == "1":
            # sign up form
            signUp.getPersonalData()
            break
        elif choice == "2":
            # login form
            login.emailLogin()
            break
        else:
            print("Invalid choice")
            continue
