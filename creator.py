import sys
import os

def dispatcher(argv):
    try:
        toCreate = argv[0]
    except IndexError:
        print("Latexhelper: No new type specified\n" + \
            "Try\n" + \
            "\tlatexhelper help\n" + \
            "to get usage information")
        sys.exit()
    if toCreate in ("-p", "project"):
        createProject()

def createProject():
    print("You are going to create a new LaTeX project")
    
    project = os.getcwd()
    project += "/" + input("Enter a name for the project: ")

    if not os.path.exists(project):
        os.makedirs(project)
