import datetime
import userDataHandling
listofProjects = userDataHandling.read_jaon(
    "./Crowd-Funding_console-app/json/projects.json")


def validatetimeinput():
    while True:
        # input date
        date_string = input('\nType the date (eg: 2023-02-15): ')
        # giving the date format
        date_format = '%Y-%m-%d'
        # using try-except blocks for handling the exceptions
        try:
            # formatting the date using strptime() function
            dateObject = datetime.datetime.strptime(date_string, date_format)
            return dateObject.date()
        # If the date validation goes wrong
        except ValueError:
            # printing the appropriate text if ValueError occurs
            print("Incorrect data format, should be YYYY-MM-DD")


def handleSearch():
    if len(listofProjects) > 0:
        inputTimeToSearch = validatetimeinput()
        # showing the projects
        for i, p in enumerate(listofProjects):
            print(p['creation_date'])
            if p['creation_date'] == inputTimeToSearch:
                print("\n   **  listing projects     **    \n")
                print(
                    f"[{i+1}] Title:{p['title']}  Details:{p['details']}   Target:{p['target']} ")
                break
            else:
                print('No such projects in that date')
                break
    else:
        print('\n NO projects yet  \n be the first user to create a project \n')


# handleSearch()
