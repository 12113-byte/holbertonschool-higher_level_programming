#!/usr/bin/python3
length = len(argv)
if __name__ = "__main__":
    print("{} arguments.".format(length))
    if length > 0:
        if length == 1:
            print("{} argument:\n{}: {}".format(length, argv[i+1], argv[i]))
        else:
            print("{} arguments:".format(length))
            for i in range(length):
                print("{}: {}".format(length[i+1], argv[i+1]))
    else:
        print("{} arguments.".format(length))
