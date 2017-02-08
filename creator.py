import os

def createProject():
    print("You are going to create a new LaTeX project")
    project = input("Enter a name for the project: ")
    if not os.path.exists(project):
        os.makedirs(project)
