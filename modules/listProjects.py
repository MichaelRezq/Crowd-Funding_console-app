import userDataHandling
listofProjects = userDataHandling.read_jaon("./modules/json/projects.json")


def listingProjects():
    if len(listofProjects) > 0:
        print("\n   **  listing projects    **    \n")
        # showing the projects
        for i, p in enumerate(listofProjects):
            print(
                f"[{i+1}] Title:{p['title']}  Details:{p['details']}   Target:{p['target']} ")
    else:
        print('\n NO projects yet  \n be the first user to create a project \n')
