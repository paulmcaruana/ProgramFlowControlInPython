if 0:
    print("True")   # 0 always evaluates to false as you will see in the output
else:
    print("False")

    name = input("Please enter your name: ")
    # if name:              It is better to write this as below until very comfortable
    if name != "":
        print("Hello, {}".format(name))
    else:
        print("Are you the man with no name?")