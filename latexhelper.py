#!/usr/bin/env python3

import sys

import creator
import messages

def main():
	dispatcher(sys.argv[1:])

def dispatcher(argv):
    try:
        command = argv[0]
    except IndexError:
        messages.helpMessage("No command specified")
        sys.exit()
    if command in ("-n", "new"):
        creator.dispatcher(argv[1:])
    else:
        messages.helpMessage("The specified command is unknown")
        sys.exit()

if __name__ == "__main__":
    main()
