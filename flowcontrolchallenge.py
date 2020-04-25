choice = "-" # this sets choice to something we don't need or will use...its declaring it
# while True: changing this to a condition
while choice !=0: # change the if and elif below
    # if choice == "0":
    #    break
    # elif
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tHave Dinner")
        print("5:\tGo to Bed")
        print("0:\tExit")

    choice = input()