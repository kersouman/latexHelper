import os
import shutil
import sys

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
    cacheFolder = projectPath + "/.latexhelper"
    preambleFolder = projectPath + "/preamble"
    preambleFile = projectPath + "/preamble.tex"

    softPath = os.path.dirname(__main__)
    originPreamblePath = softPath + "/latex_files/preamble.tex"
    originPreambleFolderPath = softPath + "/latex_files/preamble"

    if not os.path.exists(projectPath):
        os.makedirs(projectPath)
        os.makedirs(cacheFolder)
        shutil.copyfile(originPreamblePath, preambleFile)
        shutil.copy(originPreambleFolderPath, preambleFolder)
    else:
        print("The project " + projectName + " already exists")

