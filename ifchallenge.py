name = input("Please tell me your name: ")
age = int(input("Hi {}, what age are you? ".format(name)))

if 18 <= age < 31:
    print("Welcome to your holiday {}.".format(name))
else:
    print("I'm sorry you are not in the correct age group for this holiday. You would enjoy another one much better")


# The solution on the course is:
#
# name = input("Please enter your name: ")
# age = int(input("How old are you: "))
#
# if 18 <= age < 31:
#     print("Welcome to club 18-30 holidays, {0}".format(name))
# else:
#     print("I'm sorry, our holidays are only for cool people")

