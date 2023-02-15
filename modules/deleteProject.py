import userDataHandling

listOfProjects = userDataHandling.read_jaon("./modules/json/projects.json")
onlineuserEmail = userDataHandling.read_jaon(
    "./modules/json/onlineUsers.json")
listOfUserProjects = []
# print(onlineuserEmail["useremail"])

# create projects list


def createlistofuserprojects():
    for p in listOfProjects:
        # print(p)
        if p["email"] == onlineuserEmail["useremail"]:
            listOfUserProjects.append(p)


# list the projects


def listProjects():
    print(" **  your projects choose to delete  **  ")

    for p in listOfUserProjects:
        print(f"project title : {p['title']}")


# delete from list


def delletefromlist():
    while True:
        choice = input('type your project title to delete: ')
        for p in listOfUserProjects:
            if p['title'] == choice:
                listOfProjects.remove(p)
                userDataHandling.write_json(
                    listOfProjects, "./modules/json/projects.json")
                print(f'your project {p["title"]} deleted successfully')
                break
            else:
                print("type a valid project title")
                continue
        break

# handling all


def handlingDelete():
    createlistofuserprojects()
    if len(listOfUserProjects) > 0:
        listProjects()
        delletefromlist()
    else:
        print("LOoks like you don't have any projects , try create new project")
