import sys
import os

import messages

def dispatcher(argv):
    try:
        toCreate = argv[0]
    except IndexError:
        messages.helpMessage("No new type specified")
        sys.exit()
    if toCreate in ("-p", "project"):
        createProject()

def createProject():
    print("You are going to create a new LaTeX project")
    projectName = input("Enter a name for the project: ")

    projectPath = os.getcwd() + "/" + projectName

    if not os.path.exists(projectPath):
        os.makedirs(projectPath)
    else:
        print("The project " + projectName + " already exists")
