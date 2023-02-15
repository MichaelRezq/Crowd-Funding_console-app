import userDataHandling
import datetime
from createproject import inputData
listOfProjects = userDataHandling.read_jaon(
    "./Crowd-Funding_console-app/json/projects.json")
onlineuserEmail = userDataHandling.read_jaon(
    "./Crowd-Funding_console-app/json/onlineUsers.json")
listOfUserProjects = []
projectData = {}

# print(onlineuserEmail["useremail"])

# [1] create projects list


def createlistofuserprojects():
    for p in listOfProjects:
        # print(p)
        if p["email"] == onlineuserEmail["useremail"]:
            listOfUserProjects.append(p)


# [2] list the projects


def listProjects():
    print(" **  your projects choose to update  **  ")

    for p in listOfUserProjects:
        print(f"project title : {p['title']}")


# [3] update from list

def updateFromList():
    while True:
        # ask the user to input the project title
        choice = input('type your project title to update: ')
        # loop in the list of user projects
        for p in listOfUserProjects:
            # check if the title matches any of user projects
            if p['title'] == choice:
                # ask the user to  input the project data
                print("     updating  project        ")
                inputData()
                # update the value of the project in the list of all projects
                listOfProjects[listOfProjects.index(p)] = projectData
                # add the email of logged in user to the project dictionary
                useremail = userDataHandling.read_jaon(
                    "./Crowd-Funding_console-app/json/onlineUsers.json")
                projectData["email"] = useremail["useremail"]
                # add date of project creation
                projectData["creation_date"] = datetime.datetime.now()
                # write the file with the  list after update
                userDataHandling.write_json(
                    listOfProjects, "./Crowd-Funding_console-app/json/projects.json")
                print(f'your project {p["title"]} updated successfully')
                # break
                break
            else:
                # if the user  inputs any other data
                print("type a valid project title")
                break
        break

# [4] handling all functions


def handlingUpdate():
    createlistofuserprojects()
    if len(listOfUserProjects) > 0:
        listProjects()
        updateFromList()
    else:
        print("LOoks like you don't have any projects to update , try create new project")
