
import userDataHandling
import datetime
import userDataHandling
projectData = {}


def inputData():
    # create list of titles to prevent dublication of project titles
    listofprojects = userDataHandling.read_jaon('./modules/json/projects.json')
    listofprojectstitles = []
    if len(listofprojects) > 0:
        for p in listofprojects:
            listofprojectstitles.append(p["title"])
        # print the existing project titles
        print('\n ---- Already existing projects-----')
        for i, p in enumerate(listofprojectstitles):
            print(f"[{i+1}] {p}")
    # input the title
    while True:
        title = input('input your title: ')
        if title.isalpha():
            if any(listofprojectstitles) == title:
                print('ops the title is already exist')
                break
            else:
                projectData["title"] = title
                break
        else:
            print("type a valid title")
            continue

        # input the details
    while True:
        details = input('input your details: ')
        if details.isalpha():
            projectData["details"] = details
            break
        else:
            print("type a valid details")
            continue
    # input the Total target
    while True:
        target = input(
            'input your Total target (must be between(10k EG to 100k EG)): ')
        if target.isdigit() and 10000 < int(target) > 100000:
            projectData["target"] = f'{target} EG'
            break
        else:
            print("type a valid target")
            continue


def createProject():
    print("     creating project        ")
    inputData()
    print('You created your project successfully')
    # add the email of the online user to the project dictionary
    useremail = userDataHandling.read_jaon("./modules/json/onlineUsers.json")
    projectData["email"] = useremail["useremail"]
    # add date of project creation
    projectData["creation_date"] = str(datetime.datetime.now().date())
    userDataHandling.append_json(projectData, "./modules/json/projects.json")


# • Title
# • Details
# • Total target (i.e 250000 EGP)
# • Set start/end time for the campaign (validate the date formula)
