#!/usr/bin/env python3

import sys
import getopt
import creator

def main():
	dispatcher(sys.argv[1:])

def dispatcher(argv):
    try:
        command = argv[0]
    except IndexError:
        print("Latexhelper: No command specified\n" + \
            "Try\n" + \
            "\tlatexhelper help\n" + \
            "to get usage information")
        sys.exit()
    if command in ("-n", "new"):
        creator.dispatcher(argv[1:])
    else:
        print("Latexhelper: The specified command is unknown\n" + \
            "Try\n" + \
            "\tlatexhelper help\n" + \
            "to get usage information")
        sys.exit()

if __name__ == "__main__":
    main()
