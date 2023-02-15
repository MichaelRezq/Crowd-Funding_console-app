# first show menu to the user to create  or list or delete or update
import createproject
import updateProject
import deleteProject
import listProjects
import searchbytime


def showoptions():
    print("              welcome to our company            \n")
    while True:
        print('[1] to list projects   \n[2] to create project \n[3] to update project \n[4] to delete project\n[5] to search by date\n ')
        choice = input(
            "Type Ur choice number => ")
        if choice == "1":
            # listProjects
            listProjects.listingProjects()
            continue
        elif choice == "2":
            # createproject
            createproject.createProject()
            continue
        elif choice == "3":
            # updateProject
            updateProject.handlingUpdate()
            continue
        elif choice == "4":
            # deleteProject
            deleteProject.handlingDelete()
            continue
        elif choice == "5":
            # search for a project by date
            searchbytime.handleSearch()
            continue
        else:
            print("Invalid choice")
            continue
