import sys
import getopt
import creator

def main():
    arg = sys.argv[1]
    if arg == '-h':
        print('test.py -n')
        sys.exit()
    elif arg in ("-n", "--new"):
        creator.createProject()

if __name__ == "__main__":
    main()
